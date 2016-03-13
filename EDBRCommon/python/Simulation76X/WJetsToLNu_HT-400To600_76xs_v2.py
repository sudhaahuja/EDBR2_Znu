import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/0CF84FB8-2CBC-E511-B255-001EC9AF22C6.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/16DC2E82-2CBC-E511-A636-D4AE526A0455.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/1CB2044C-29BC-E511-A0E7-001EC9AF2064.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/2203364D-22BC-E511-8A21-00221961CD22.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/26421AFD-36BC-E511-A11F-D4AE526A0A39.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/320F4549-3CBC-E511-A92D-001EC9B215C4.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/4A150A17-27BC-E511-918A-D4AE526A0922.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/4A7A0F6B-22BC-E511-8604-001EC9B2147A.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/56440314-2DBC-E511-9EC9-1CC1DE192802.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/58797762-29BC-E511-802F-842B2B75FFFD.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/62E63C4F-2DBC-E511-81E7-D4AE526A0CFB.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/68861D79-2CBC-E511-B781-842B2B7682C7.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/6C6957F8-36BC-E511-9663-842B2B766849.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/6E1F2780-3BBC-E511-A14D-1CC1DE18D40A.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/7496B3EB-2FBC-E511-BAA9-842B2B760921.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/80854D64-22BC-E511-8A7A-D4AE5269F5FF.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/8C9A8E93-3BBC-E511-886F-001EC9B63C08.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/9238C190-44BC-E511-938A-1CC1DE19283E.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/92BCDA39-1CBC-E511-A285-D4AE526A0CFB.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/92EB3A2C-27BC-E511-8D59-00221961CD22.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/949163F5-32BC-E511-BC56-D4AE526A03AD.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/98061522-27BC-E511-8F8D-1CC1DE18CFF0.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/A43D55F7-41BC-E511-BD2E-D4AE526A0A4B.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/AA4293DE-34BC-E511-99FE-D4AE526A0B29.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/B0D30C13-27BC-E511-A4C6-0CC47A00934A.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/B22FA5EB-2FBC-E511-9642-842B2B760921.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/BA0F2C71-22BC-E511-A56C-001EC9AF22D5.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/BCBED76C-3DBC-E511-ACCD-842B2B75FDA9.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/E4F68061-1CBC-E511-8558-842B2B765E01.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/E68F48E9-3BBC-E511-9576-D4AE526A048B.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/3475E248-B3BD-E511-9221-001EC9B20F8E.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/3C4E7E4E-B3BD-E511-BFAF-D4AE526A05C8.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/5EA62442-B3BD-E511-9CDB-00221965B5AC.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/6669734B-B3BD-E511-83D8-842B2B758BAA.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/68782754-B3BD-E511-A25C-D4AE526A023A.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/8A5DC540-B3BD-E511-9A72-782BCB161FC2.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/A4B91F1A-B4BD-E511-B7C6-D4AE526A0419.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/A8CBF15F-B3BD-E511-9545-D4AE526A1010.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/B258854E-B3BD-E511-8596-001EC9B1D3C6.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/BC67C248-B3BD-E511-8289-001EC9AF2055.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/BE0DC449-B3BD-E511-801B-D4AE5269F656.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/BEFE934C-B3BD-E511-82FE-D4AE526A0AB5.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/C416014E-B3BD-E511-AB0D-0CC47A01035C.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/DC492C4B-B3BD-E511-B5D9-D4AE5269F656.root',
       '/store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/70000/EE31414B-B3BD-E511-8C1C-1CC1DE18C97E.root' ] );


secFiles.extend( [
               ] )


