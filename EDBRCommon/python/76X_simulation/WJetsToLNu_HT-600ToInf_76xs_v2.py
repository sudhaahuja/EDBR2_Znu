import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0E84E437-DEBD-E511-8230-00259048A862.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0ECBC893-DEBD-E511-B5C4-003048322C5D.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0ED22D2C-DFBD-E511-8BF9-00259019A41E.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/1E6BAFED-DEBD-E511-9F55-002590791D36.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/2AA6B8B1-DEBD-E511-8E41-002590D9D9A4.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/320ADCC7-DEBD-E511-82F4-002590D9D9BC.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/3AD1B1AA-DEBD-E511-878D-0025901ABD18.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/4AF7F345-DFBD-E511-B4BE-0025907E343C.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/583EF7C0-DEBD-E511-B328-002590D9D8B6.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/5A9BE078-DEBD-E511-8F61-00259048AC98.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/60D629A3-DEBD-E511-9B20-0CC47A57D168.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/702717AA-DEBD-E511-830B-00304867FD63.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/72B0544A-DFBD-E511-A999-00304834BB18.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/72CC33BE-DEBD-E511-B6B8-0CC47A57D036.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/7A0291B0-DDBD-E511-87A8-00304867FDCB.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/7C6845AC-DEBD-E511-A0E2-0025901AC0FA.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/906D7536-DEBD-E511-926D-0025901AC1F8.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/9E128B04-DEBD-E511-ADD3-003048CB8768.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/BC4E4621-DEBD-E511-934A-0025901AC3F8.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/CCEC9CB8-DDBD-E511-A268-0CC47A57CC8A.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/E2AEAE7D-DEBD-E511-8341-00259048A862.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/E47314E7-DEBD-E511-8C2E-0025907D1D6C.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/F0BDD5B6-DEBD-E511-8A03-0025901AC3F6.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/FAB5873E-DFBD-E511-AA63-0025901AC404.root' ] );


secFiles.extend( [
               ] )

