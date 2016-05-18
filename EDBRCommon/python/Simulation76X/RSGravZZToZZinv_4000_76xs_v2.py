import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4000_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/02495DFF-87D9-E511-AE4F-44A84225C7BB.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4000_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/189ED804-88D9-E511-8849-002590747DA2.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4000_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/1E14BCAF-87D9-E511-B51A-002590D9D8B2.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4000_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/B4259FFC-87D9-E511-8012-002590D4FC42.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4000_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/FA8116B1-87D9-E511-A687-02163E012F5F.root' ] );


secFiles.extend( [
               ] )


