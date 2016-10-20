import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4500_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/082B5B26-70DA-E511-B9C3-0CC47A4C8F10.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4500_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/6A480020-70DA-E511-B7E6-B083FED76DB1.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4500_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/AEEB0DCB-84DA-E511-A4E1-003048C56E68.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4500_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/B6CF543A-83DA-E511-B04A-003048C56E68.root',
       '/store/mc/RunIIFall15MiniAODv2/RSGravToZZToZZinv_narrow_M-4500_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/BABD48DF-70DA-E511-903B-20CF3019DF19.root' ] );


secFiles.extend( [
               ] )
