import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
B="#0A5AC8"
fig,ax=plt.subplots(figsize=(11,6.2),dpi=170); ax.set_xlim(0,110); ax.set_ylim(0,62); ax.axis("off")
ax.add_patch(Rectangle((0,0),110,62,fc="#F4F6FA",ec="#999",lw=1))
# map area
ax.add_patch(Rectangle((32,2),76,58,fc="#EAEFE6",ec="#bbb"))
import random; random.seed(3)
for x in range(34,106,12):
    for y in range(4,58,11):
        w=random.randint(6,9); h=random.randint(5,8)
        ax.add_patch(Rectangle((x,y),w,h,fc="#C9CED6",ec="none"))
        if random.random()<.5: ax.add_patch(Rectangle((x+w,y-1),4,h,fc="#7C8594",alpha=.35,ec="none"))  # shadows
def line(pts,c,lw,ls="-"): ax.plot([p[0] for p in pts],[p[1] for p in pts],c=c,lw=lw,ls=ls,solid_capstyle="round")
short=[(38,8),(38,30),(70,30),(100,52)]
shade=[(38,8),(44,8),(44,50),(70,50),(100,52)]
line(short,"#E8A400",4); line(shade,B,4)
ax.add_patch(Circle((38,8),1.6,fc="#2E7D32",ec="white")); ax.add_patch(Circle((100,52),1.6,fc="#C62828",ec="white"))
ax.text(41,10.5,"A",fontsize=9,weight="bold"); ax.text(97,54.5,"B",fontsize=9,weight="bold")
# panel
ax.add_patch(FancyBboxPatch((2,2),28,58,boxstyle="round,pad=0.2,rounding_size=1.5",fc="white",ec="#bbb"))
ax.text(4,56,"Shaded route planner",fontsize=11,weight="bold",color=B)
for i,(lab,val) in enumerate([("From","click map: A"),("To","click map: B"),("Date","DD.MM.YYYY"),("Time","HH:MM")]):
    y=50-i*7.5; ax.text(4,y+3.2,lab,fontsize=7,color="#666")
    ax.add_patch(FancyBboxPatch((4,y-1.5),24,4,boxstyle="round,pad=0.1,rounding_size=0.8",fc="#F4F6FA",ec="#ccc")); ax.text(5.2,y+0.1,val,fontsize=8)
ax.text(4,19.5+2,"Shade priority  λ",fontsize=7,color="#666")
ax.plot([5,27],[18.5,18.5],c="#bbb",lw=3); ax.plot([5,19],[18.5,18.5],c=B,lw=3); ax.add_patch(Circle((19,18.5),1.3,fc=B))
ax.text(4,15.3,"shorter",fontsize=6.5,color="#666"); ax.text(22,15.3,"shadier",fontsize=6.5,color="#666")
ax.add_patch(FancyBboxPatch((4,9.5),24,4,boxstyle="round,pad=0.1,rounding_size=0.8",fc=B,ec=B)); ax.text(16,11.4,"Build routes",fontsize=9,color="white",ha="center",va="center",weight="bold")
ax.text(4,5.2,"Max detour: +30 %",fontsize=7,color="#666")
# route cards (right overlay)
cards=[("Shortest","#E8A400","X m · Y % shade · +0 %"),("Balanced",B,"X m · Y % shade · +Z %"),("Shadiest","#0B8F6B","X m · Y % shade · +Z %")]
for i,(n,c,t) in enumerate(cards):
    y=19-i*7
    ax.add_patch(FancyBboxPatch((72,y-2.5),35,6,boxstyle="round,pad=0.1,rounding_size=0.8",fc="white",ec=c,lw=1.6))
    ax.text(74,y+1.6,n,fontsize=8,weight="bold",color=c); ax.text(74,y-1.2,t,fontsize=7,color="#444")
ax.add_patch(FancyBboxPatch((72,25),35,4.2,boxstyle="round,pad=0.1,rounding_size=0.8",fc="white",ec="#ccc"))
ax.plot([74,78],[27,27],c=B,lw=3); ax.text(79,26.6,"shade",fontsize=7); ax.plot([88,92],[27,27],c="#E8A400",lw=3); ax.text(93,26.6,"sun",fontsize=7)
ax.text(54,0.2,"schematic mock-up, values X/Y/Z are placeholders",fontsize=6.5,color="#666",ha="center")
plt.savefig("mock.png",bbox_inches="tight",facecolor="white")
