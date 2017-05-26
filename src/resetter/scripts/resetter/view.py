
import pymel.core as pm
import logging

from core import *

__all__ = [
	"GUI",
]

LOG = logging.getLogger('resetter')
LOG.setLevel(logging.INFO)


class GUI(object):
    def __init__(self):
        self.winName = 'boResetterWin'
        #define colors
        self.colSet = [0.3, 0.36, 0.49]
        self.colRemove = [0.49, 0.3, 0.3]
        self.colReset = [0.2, 0.2, 0.2]
        self.colReset2 = [0.25, 0.25, 0.25]
        self.build()
    
    def build(self):
        #check for pre-existing window
        if pm.window(self.winName, ex=True):
            pm.deleteUI(self.winName, wnd=True)
        
        if not pm.windowPref(self.winName, ex=True):
            pm.windowPref(self.winName, tlc=(200, 200))
        pm.windowPref(self.winName, e=True, w=280, h=100)
        
        with pm.window(self.winName, rtf=1, mb=1, tlb=True, t='Resetter') as self.win:
            imenu = pm.menu(l='Info')
            pm.setParent(imenu, m=True)
            pm.menuItem(l='List Objects with Defaults', c=pm.Callback(listObjectsWithDefaults))
            pm.menuItem(l='Select Objects with Defaults', c=pm.Callback(selectObjectsWithDefaults))
            pm.menuItem(l='List Defaults', c=pm.Callback(listDefaults))
            
            with pm.formLayout(nd=100) as form:
                
                with pm.frameLayout(l='Set/Remove Defaults', bs='out', mw=2, mh=2, cll=True, cl=True) as setFrame:
                    with pm.columnLayout(rs=2, adj=True):
                        pm.button(l='Set Defaults', c=pm.Callback(setDefaults), bgc=self.colSet, ann='Set defaults on the selected objects using all keyable attributes')
                        pm.button(l='Set Defaults Include Non-Keyable', c=pm.Callback(setDefaultsNonkeyable), bgc=self.colSet, ann='Set defaults on the selected objects using keyable and non-keyable attributes in the channel box')
                        pm.button(l='Set Defaults with CB Selection', c=pm.Callback(setDefaultsCBSelection), bgc=self.colSet, ann='Set defaults on the selected objects using the selected channel box attributes')
                        pm.button(l='Remove Defaults', c=pm.Callback(removeDefaults), bgc=self.colRemove, ann='Remove all defaults from the selected objects')
                        pm.button(l='Remove from All Objects', c=pm.Callback(removeAllDefaults), bgc=self.colRemove, ann='Remove defaults from all objects in the scene')
                
                with pm.frameLayout(l='Reset', bs='out', mw=2, mh=2) as resetFrame:
                    with pm.formLayout(nd=100) as resetForm:
                        b6 = pm.button(l='Smart', c=pm.Callback(resetSmart), bgc=self.colReset, ann='Reset the selected objects. Uses transform standards if no defaults are defined for translate, rotate, and scale')
                        b7 = pm.button(l='Default', c=pm.Callback(reset), bgc=self.colReset, ann='Reset the selected objects using only stored defaults, if any')
                        b8 = pm.button(l='Transform', c=pm.Callback(resetTransform), bgc=self.colReset, ann='Reset the selected objects using only transform standards for translate, rotate, scale (eg. 0, 0, 1)')
                        b9 = pm.button(l='All', c=pm.Callback(resetAll), bgc=self.colReset2, ann='Reset all objects in the scene with defaults')
                        pm.formLayout(resetForm, e=True,
                            ap=[(b6, 'left', 0, 0), (b6, 'right', 2, 25),
                                (b7, 'left', 2, 25), (b7, 'right', 2, 50),
                                 (b8, 'left', 2, 50), (b8, 'right', 2, 75),
                                  (b9, 'left', 2, 75), (b9, 'right', 2, 100), ])
                
                mw = 4
                pm.formLayout(form, e=True,
                    af=[(setFrame, 'left', mw), (setFrame, 'right', mw),
                        (resetFrame, 'left', mw), (resetFrame, 'right', mw)],
                    ac=[(resetFrame, 'top', 2, setFrame)],  )

