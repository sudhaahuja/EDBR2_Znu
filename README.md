Instructions to setup the ExoDiBosonResonances code
========

```
cmsrel CMSSW_7_4_15_patch1
cd CMSSW_7_4_15_patch1/src
cmsenv
git cms-init # This will allow you to checkout packages in official CMSSW
git clone -b master git@github.com:dromeroa/EDBR2_Znu.git ExoDiBosonResonances
scram b -j 10
```

