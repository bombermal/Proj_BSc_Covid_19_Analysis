# -*- coding: utf-8 -*-
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

def three_plots(conditions, list_of_filtered_dfs, name_id, full_or_simple=False):
    fig, (ax1, ax2, ax3 ) = plt.subplots(3,1, figsize=(90, 30), dpi=320, sharex=True)
    aux = [ax1, ax2, ax3]
    alpha = .7
    
    for ii, jj, tb in zip(aux, conditions, list_of_filtered_dfs):
      ii.set_title("SNPs "+str(jj)+"%")
      ii.xaxis.set_major_locator(ticker.FixedLocator(range(1,29400, 999)))
      
      ii.plot('Pos', 'A', data=tb, alpha=alpha)
      ii.plot('Pos', 'C', data=tb, alpha=alpha)
      ii.plot('Pos', 'T', data=tb, alpha=alpha)
      ii.plot('Pos', 'G', data=tb, alpha=alpha)
      if full_or_simple:
        ii.plot('Pos', 'N', data=tb, alpha=alpha)
        ii.plot('Pos', '-', data=tb, alpha=alpha)
        ii.plot('Pos', 'W', data=tb, alpha=alpha)
        ii.plot('Pos', 'R', data=tb, alpha=alpha)
        ii.plot('Pos', 'Y', data=tb, alpha=alpha)
        ii.plot('Pos', 'S', data=tb, alpha=alpha)
        ii.plot('Pos', 'M', data=tb, alpha=alpha)
        ii.plot('Pos', 'K', data=tb, alpha=alpha)
        ii.plot('Pos', 'V', data=tb, alpha=alpha)
        ii.plot('Pos', 'H', data=tb, alpha=alpha)
    
    ax2.legend(loc=2)
    if full_or_simple:
        plt.savefig("Img/Full_"+str(name_id)+"_"+'-'.join(str(x) for x in conditions)+".png", dpi=320)
    else:
        plt.savefig("Img/Semi_"+str(name_id)+"_"+'-'.join(str(x) for x in conditions)+".png", dpi=320)
    
    #plt.plot()