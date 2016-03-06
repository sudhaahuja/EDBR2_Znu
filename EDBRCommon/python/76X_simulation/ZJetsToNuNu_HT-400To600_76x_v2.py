import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/12620DCF-03CE-E511-9238-02163E00B4EB.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/16C163C0-03CE-E511-ADE8-02163E012DB7.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/18DD7FAE-03CE-E511-9A2F-02163E017954.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/34471024-04CE-E511-B5A3-02163E0176E7.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/347FE1C2-C0CD-E511-8E61-001E67E95C64.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/447475E9-F6CD-E511-B4ED-02163E013203.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/4A4A98E8-FDCD-E511-B92C-02163E00E658.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/5CC922D1-03CE-E511-A5D7-02163E014347.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/788A612F-FDCD-E511-AD86-02163E015CD8.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/822938F8-F0CD-E511-8CD5-02163E0164F8.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/8812BFD5-C0CD-E511-AE1C-02163E01152C.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/8E6A8FD2-03CE-E511-878B-02163E016845.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/B0B9D5B4-05CE-E511-B705-02163E01318B.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/B698D0B8-03CE-E511-83EF-02163E01778B.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/B82B5DD8-03CE-E511-B6C5-02163E01143F.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/BCF42BF3-FCCD-E511-B779-02163E0164D6.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/CA575F06-04CE-E511-858B-02163E01318B.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/CA7A97C4-03CE-E511-90DE-02163E013C70.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/D6FA84D2-03CE-E511-A0E3-02163E013160.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/D859951C-FDCD-E511-BB74-02163E01306C.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/E4C5A2CC-03CE-E511-B50C-02163E0166F7.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/EAD5E5C8-03CE-E511-83EF-02163E013209.root',
       '/store/mc/RunIIFall15MiniAODv2/ZJetsToNuNu_HT-400To600_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/FE1B23EB-03CE-E511-BCEC-02163E011553.root' ] );


secFiles.extend( [
               ] )

