import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(6); n=2000
cov=rng.poisson(30,n).astype(float)
cov[800:850]*=0.1  # dropout
cov[1400:1450]*=3  # repeat pileup
plt.figure(figsize=(9,3)); plt.fill_between(range(n),cov,alpha=.4); plt.plot(cov,lw=.6)
plt.axhline(cov.mean(),ls="--",c="k",label=f"mean {cov.mean():.0f}x")
plt.xlabel("position (bp)"); plt.ylabel("read depth"); plt.title("Coverage profile (demo data)"); plt.legend()
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write(f"mean depth {cov.mean():.1f}x\n"); print("ok")