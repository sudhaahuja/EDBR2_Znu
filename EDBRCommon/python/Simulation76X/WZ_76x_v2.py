import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/08D64252-85BB-E511-A3A6-74867AD4BDEC.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/20FE815A-85BB-E511-A9EE-74867AD4B754.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/3285315D-85BB-E511-B2EE-74867AD4EF3C.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/38058952-85BB-E511-8CD5-74867AD4BDEC.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/5C1F985A-85BB-E511-9860-74867AD4B754.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/74EBAB53-85BB-E511-AB0C-74867AD4BDEC.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/8E2F3A58-85BB-E511-BC3D-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/A09AAE57-85BB-E511-9970-74867AD4DD04.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/04E1D13B-90BD-E511-8E4B-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/1C0F0142-92BD-E511-9138-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/1C8FE0CA-8BBD-E511-B4B6-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/28D9EBC1-1ABD-E511-8B88-74867AD4BE94.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/2E843831-7BBD-E511-901F-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/34EE9491-8FBD-E511-975F-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/3CC261E0-8DBD-E511-A6F0-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/503022DB-8CBD-E511-AC85-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/54F41B54-93BD-E511-96BB-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/5A30EEB7-8EBD-E511-87BB-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/5AE2AE3D-91BD-E511-82FA-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/6200CC26-79BD-E511-8B05-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/68B16194-19BD-E511-B692-74867AD4BE94.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/748313DE-8ABD-E511-B507-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/768DE513-7CBD-E511-821D-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/82958A52-7ABD-E511-8905-74867AD4BE90.root',
       '/store/mc/RunIIFall15MiniAODv2/WZ_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/EAA1679C-A8BC-E511-B776-74867AD4BE90.root' ] );


secFiles.extend( [
               ] )


