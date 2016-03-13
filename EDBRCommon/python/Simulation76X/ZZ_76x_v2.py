import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0416A52C-5BB8-E511-AC67-02163E0166FE.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/087B9F75-5EB8-E511-B9ED-02163E011DD3.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0CFD1897-5BB8-E511-8AEB-02163E00F8C5.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/20318A7E-5BB8-E511-B982-02163E00F3C4.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/52100F5C-5BB8-E511-92FB-02163E011BD3.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/5838060A-5BB8-E511-A7F5-02163E00F47F.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/5C449DE5-5AB8-E511-BB82-02163E013220.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/5CC77228-5BB8-E511-8F1E-02163E01797E.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/60292D16-5CB8-E511-A999-02163E016C20.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/642E93ED-5BB8-E511-8C83-02163E01797E.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/6A9DCE38-5BB8-E511-A481-02163E0164A4.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/743E0FA7-5BB8-E511-AEC4-02163E016513.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/762E9E4E-5BB8-E511-BF53-02163E016922.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/7C9883EF-5AB8-E511-9A74-02163E013CF5.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/8CC52AE7-5BB8-E511-A68B-02163E01663D.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/B45C2D49-5BB8-E511-81FF-02163E0177FA.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/C06CDF1A-5CB8-E511-8DB5-02163E014803.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/D43A2CBA-5BB8-E511-B598-02163E0165C0.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/D68DDBF0-5CB8-E511-9F2B-02163E0137ED.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/E2D40141-5CB8-E511-AB53-001E67E95BFA.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/F0995DEA-5BB8-E511-9468-02163E0168FC.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/F405D606-5CB8-E511-B77B-02163E016C35.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/FA6C4661-5BB8-E511-B328-02163E01643A.root',
       '/store/mc/RunIIFall15MiniAODv2/ZZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/FAF666DE-5BB8-E511-BF6F-02163E013220.root' ] );


secFiles.extend( [
               ] )

