import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/WprimeToWZ_width0p1_M-4000_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/20000/4E1E3F1C-F3C1-E511-BEFA-008CFA1CB55C.root',
       '/store/mc/RunIIFall15MiniAODv2/WprimeToWZ_width0p1_M-4000_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/20000/520B8819-E9C1-E511-AC60-001CC4A65D70.root',
       '/store/mc/RunIIFall15MiniAODv2/WprimeToWZ_width0p1_M-4000_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/20000/5AC24747-7EC1-E511-BFD2-001E67D8A423.root',
       '/store/mc/RunIIFall15MiniAODv2/WprimeToWZ_width0p1_M-4000_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/20000/9A385789-F3C1-E511-9924-6C3BE5B54138.root' ] );


secFiles.extend( [
               ] )

