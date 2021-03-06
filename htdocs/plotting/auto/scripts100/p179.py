"""GDD Accumulation"""
import datetime

import numpy as np
import pandas as pd
from pyiem.util import get_autoplot_context, get_dbconn
from pyiem.network import Table as NetworkTable


def get_description():
    """ Return a dict describing how to call this plotter """
    desc = dict()
    desc['data'] = True
    desc['description'] = """this application creates two 2-D histograms of
    GDD accumulation frequencies. These frequencies are based on historical
    data for the specificed site and base the end of each year's growing
    season on the first sub freezing temperature of the fall.  The left hand
    plot shows the overall frequency based on each year's data.  The right
    hand plot does a scenario using the combination of year to date data for
    this year and then each previous year afterwards is appended to this
    year's data to provide frequencies.  The right hand plot is meant to
    provide current frequencies / probabilities of what could potentially
    happen this year.
    """
    desc['arguments'] = [
        dict(type='station', name='station', default='IA2203',
             label='Select Station:', network='IACLIMATE'),
        dict(type='int', name='gddbase', default=2300,
             label='Growing Degree Days to Accumulate:'),
        ]
    return desc


def plotter(fdict):
    """ Go """
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    import matplotlib.colors as mpcolors
    ctx = get_autoplot_context(fdict, get_description())
    station = ctx['station']
    gddbase = ctx['gddbase']
    nt = NetworkTable(ctx['network'])
    today = datetime.datetime.now()
    byear = nt.sts[station]['archive_begin'].year
    eyear = today.year + 1
    pgconn = get_dbconn('coop')
    cursor = pgconn.cursor()
    table = "alldata_%s" % (station[:2],)
    cursor.execute("""SELECT year, extract(doy from day),
        gddxx(50, 86, high,low), low
         from """+table+""" where station = %s and year > %s
         """, (station, byear))

    gdd = np.zeros((eyear-byear, 366), 'f')
    freezes = np.zeros((eyear-byear), 'f')
    freezes[:] = 400.0

    for row in cursor:
        gdd[int(row[0]) - byear, int(row[1]) - 1] = row[2]
        if row[1] > 180 and row[3] < 32 and row[1] < freezes[row[0] - byear]:
            freezes[int(row[0]) - byear] = row[1]

    for i, freeze in enumerate(freezes):
        gdd[i, int(freeze):] = 0.0

    idx = int(datetime.datetime.now().strftime("%j")) - 1
    apr1 = int(datetime.datetime(2000, 4, 1).strftime("%j")) - 1
    jun30 = int(datetime.datetime(2000, 6, 30).strftime("%j")) - 1
    sep1 = int(datetime.datetime(2000, 9, 1).strftime("%j")) - 1
    oct31 = int(datetime.datetime(2000, 10, 31).strftime("%j")) - 1

    # Replace all years with the last year's data
    scenario_gdd = gdd * 1
    scenario_gdd[:-1, :idx] = gdd[-1, :idx]

    # store our probs
    probs = np.zeros((oct31 - sep1, jun30 - apr1), 'f')
    scenario_probs = np.zeros((oct31 - sep1, jun30 - apr1), 'f')

    rows = []
    for x in range(apr1, jun30):
        for y in range(sep1, oct31):
            sums = np.where(np.sum(gdd[:-1, x:y], 1) >= gddbase, 1, 0)
            probs[y-sep1, x-apr1] = sum(sums) / float(len(sums)) * 100.0
            sums = np.where(np.sum(scenario_gdd[:-1, x:y], 1) >= gddbase,
                            1, 0)
            scenario_probs[y-sep1, x-apr1] = (
                sum(sums) / float(len(sums)) * 100.0)
            rows.append(dict(x=x, y=y, prob=probs[y-sep1, x-apr1],
                             scenario_probs=scenario_probs[y-sep1, x-apr1]))
    df = pd.DataFrame(rows)

    probs = np.where(probs < 0.1, -1, probs)
    scenario_probs = np.where(scenario_probs < 0.1, -1, scenario_probs)

    (fig, ax) = plt.subplots(1, 2, sharey=True, figsize=(8, 6))

    cmap = plt.get_cmap('jet')
    cmap.set_under('white')
    norm = mpcolors.BoundaryNorm(np.arange(0, 101, 5), cmap.N)

    ax[0].imshow(np.flipud(probs), aspect='auto',
                 extent=[apr1, jun30, sep1, oct31],
                 interpolation='nearest', vmin=0, vmax=100, cmap=cmap,
                 norm=norm)
    ax[0].grid(True)
    ax[0].set_title("Overall Frequencies")
    ax[0].set_xticks((91, 106, 121, 136, 152, 167))
    ax[0].set_ylabel("Growing Season End Date")
    ax[0].set_xlabel("Growing Season Begin Date")
    ax[0].set_xticklabels(('Apr 1', '15', 'May 1', '15', 'Jun 1', '15'))
    ax[0].set_yticks((244, 251, 258, 265, 274, 281, 288, 295, 305))
    ax[0].set_yticklabels(('Sep 1', 'Sep 8', 'Sep 15', 'Sep 22', 'Oct 1',
                           'Oct 8', 'Oct 15', 'Oct 22', 'Nov'))

    res = ax[1].imshow(np.flipud(scenario_probs), aspect='auto',
                       extent=[apr1, jun30, sep1, oct31],
                       interpolation='nearest', vmin=0, vmax=100, cmap=cmap,
                       norm=norm)
    ax[1].grid(True)
    ax[1].set_title("%s Scenario to %s" % (today.year,
                                           today.strftime("%-d %B")))
    ax[1].set_xticks((91, 106, 121, 136, 152, 167))
    ax[1].set_xticklabels(('Apr 1', '15', 'May 1', '15', 'Jun 1', '15'))
    ax[1].set_xlabel("Growing Season Begin Date")

    fig.subplots_adjust(bottom=0.20, top=0.85)
    cbar_ax = fig.add_axes([0.05, 0.06, 0.85, 0.05])
    fig.colorbar(res, cax=cbar_ax, orientation='horizontal')

    fig.text(0.5, 0.90,
             ("%s-%s %s GDDs\n"
              "Frequency [%%] of reaching %.0f GDDs prior to first freeze"
              ) % (byear, eyear-1,
                   nt.sts[station]['name'], gddbase), fontsize=16,
             ha='center')

    return fig, df


if __name__ == '__main__':
    plotter(dict())
