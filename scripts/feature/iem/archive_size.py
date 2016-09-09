import datetime
import matplotlib.pyplot as plt

data = """250528    2000/02/01
346308    2000/03/01
263984    2000/04/01
335016    2000/05/01
360636    2000/06/01
240368    2000/07/01
410548    2000/08/01
393456    2000/09/01
463152    2000/10/01
461328    2000/11/01
336092    2000/12/01
244284    2001/01/01
236028    2001/02/01
246912    2001/03/01
180504    2001/04/01
275700    2001/05/01
277644    2001/06/01
338808    2001/07/01
334916    2001/08/01
296244    2001/09/01
485216    2001/10/01
495740    2001/11/01
375212    2001/12/01
310176    2002/01/01
382944    2002/02/01
394776    2002/03/01
278288    2002/04/01
400956    2002/05/01
501232    2002/06/01
361456    2002/07/01
533072    2002/08/01
496040    2002/09/01
727208    2002/10/01
575364    2002/11/01
314956    2002/12/01
423760    2003/01/01
413720    2003/02/01
182256    2003/03/01
290992    2003/04/01
459764    2003/05/01
406356    2003/06/01
332108    2003/07/01
562540    2003/08/01
504564    2003/09/01
346636    2003/10/01
607092    2003/11/01
499664    2003/12/01
414780    2004/01/01
326536    2004/02/01
399616    2004/03/01
288464    2004/04/01
432024    2004/05/01
457844    2004/06/01
539544    2004/07/01
608544    2004/08/01
506428    2004/09/01
615492    2004/10/01
807240    2004/11/01
495284    2004/12/01
567816    2005/01/01
401436    2005/02/01
308528    2005/03/01
407776    2005/04/01
412300    2005/05/01
595624    2005/06/01
431048    2005/07/01
535696    2005/08/01
466200    2005/09/01
344928    2005/10/01
650228    2005/11/01
554060    2005/12/01
631944    2006/01/01
540336    2006/02/01
408488    2006/03/01
470556    2006/04/01
613820    2006/05/01
653584    2006/06/01
601124    2006/07/01
779828    2006/08/01
660344    2006/09/01
470704    2006/10/01
739728    2006/11/01
735540    2006/12/01
626064    2007/01/01
673632    2007/02/01
651055    2007/03/01
870760    2007/04/01
681004    2007/05/01
850368    2007/06/01
530316    2007/07/01
624020    2007/08/01
539412    2007/09/01
676316    2007/10/01
375704    2007/11/01
880456    2007/12/01
554184    2008/01/01
614552    2008/02/01
664740    2008/03/01
665676    2008/04/01
495052    2008/05/01
640148    2008/06/01
488032    2008/07/01
633224    2008/08/01
515140    2008/09/01
469488    2008/10/01
714960    2008/11/01
640180    2008/12/01
584844    2009/01/01
539840    2009/02/01
610968    2009/03/01
686840    2009/04/01
655136    2009/05/01
661900    2009/06/01
561800    2009/07/01
630108    2009/08/01
525672    2009/09/01
786304    2009/10/01
652108    2009/11/01
639504    2009/12/01
914912    2010/01/01
1033280    2010/02/01
983512    2010/03/01
809028    2010/04/01
1000896    2010/05/01
1123532    2010/06/01
884704    2010/07/01
926912    2010/08/01
822816    2010/09/01
855136    2010/10/01
959316    2010/11/01
2310372    2010/12/01
2108408    2011/01/01
2597752    2011/02/01
2167468    2011/03/01
2412480    2011/04/01
2633772    2011/05/01
2741588    2011/06/01
5074592    2011/07/01
5830220    2011/08/01
5576488    2011/09/01
5025732    2011/10/01
4679484    2011/11/01
5746596    2011/12/01
5885144    2012/01/01
9434080    2012/02/01
10440768    2012/03/01
11764580    2012/04/01
14935252    2012/05/01
14333220    2012/06/01
14652408    2012/07/01
14288116    2012/08/01
14695496    2012/09/01
14631568    2012/10/01
10853392    2012/11/01
9394536    2012/12/01
10938140    2013/01/01
8704624    2013/02/01
9389384    2013/03/01
11912876    2013/04/01
13314104    2013/05/01
15014032    2013/06/01
17294188    2013/07/01
15805628    2013/08/01
18090736    2013/09/01
14353456    2013/10/01
15525156    2013/11/01
11172848    2013/12/01
12781908    2014/01/01
13150604    2014/02/01
14397756    2014/03/01
14674300    2014/04/01
15832844    2014/05/01
16729728    2014/06/01
18721972    2014/07/01
19781048    2014/08/01
22784752    2014/09/01
20139536    2014/10/01
18538720    2014/11/01
16281792    2014/12/01
15144216    2015/01/01
20402968    2015/02/01
17696484    2015/03/01
16849440    2015/04/01
15795596    2015/05/01
21234868    2015/06/01
22091156    2015/07/01
20291432    2015/08/01
19017312    2015/09/01
21259324    2015/10/01
20684676    2015/11/01
20085256    2015/12/01
16077172    2016/01/01
16823996    2016/02/01
16984572    2016/03/01
20808028    2016/04/01
23953816    2016/05/01
23686664    2016/06/01
24184016    2016/07/01
22299404    2016/08/01
26626264    2016/09/01"""

dates = [datetime.date(2000, 1, 1)]
szs = [0.2]
accum = [0.0002*30.]
for line in data.split("\n"):
    tokens = line.strip().split()
    sz = float(tokens[0]) / 1000000.0
    szs.append(sz)
    accum.append(accum[-1] + 30. * sz / 1000.)
    dates.append(datetime.datetime.strptime(tokens[1], '%Y/%m/%d'))

(fig, ax) = plt.subplots(1, 1)

ax.bar(dates, szs, width=30, fc='b', ec='b')
ax2 = ax.twinx()
ax2.plot(dates, accum, lw=2, c='r')
ax2.set_ylabel("Total Archive Volume [TB]", color='r')
ax.set_ylabel("Daily Archive Volume [GB]")
ax.grid(True)
ax.set_title("IEM File-based Archive Storage (2000 - September 2016)")

ax.annotate("Add Iowa RWIS webcams", xy=(datetime.datetime(2009, 12, 1), 1.),
            xycoords='data', xytext=(-150, 30), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

ax.annotate("Add High-res NEXRAD composites",
            xy=(datetime.datetime(2010, 12, 1), 2.25),
            xycoords='data', xytext=(-200, 50), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

ax.annotate("Add GIS GINI Satellite Images",
            xy=(datetime.datetime(2011, 12, 1), 6),
            xycoords='data', xytext=(-200, 50),
            textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

ax.annotate("Add Individual NEXRAD Images",
            xy=(datetime.datetime(2012, 2, 1), 9.5),
            xycoords='data', xytext=(-200, 50), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

ax.annotate("Add Some Model Surface Analysis",
            xy=(datetime.datetime(2013, 4, 1), 13.5),
            xycoords='data', xytext=(-300, 30), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

ax.annotate("Add MRMS Products",
            xy=(datetime.datetime(2014, 6, 1), 17.5),
            xycoords='data', xytext=(-300, 30), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

ax.annotate("Increased Size of Individual NEXRADs due to SAILS",
            xy=(datetime.datetime(2016, 5, 1), 24.5),
            xycoords='data', xytext=(-400, 30), textcoords='offset points',
            bbox=dict(boxstyle="round", fc="0.8"),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=1"))

fig.savefig('test.png')
