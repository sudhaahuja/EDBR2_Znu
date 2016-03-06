import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/0EE6E0B8-FFB7-E511-B0C6-0025904CDDFA.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/107BF4B8-FFB7-E511-A109-0025905C9742.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/14B8F5B7-FFB7-E511-BB5B-0025904C540C.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/2E8004B8-FFB7-E511-AF3C-0025904B9B3C.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/408D15EC-FFB7-E511-AC76-E03F49D6226B.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/4E8737B8-FFB7-E511-BE05-0025904C66E4.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/581525BA-FFB7-E511-A3B2-003048947BB9.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/5CA667BF-FFB7-E511-A640-BCEE7B2FE035.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/6E7136B9-FFB7-E511-9E2E-0025904C637E.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/721DF1B7-FFB7-E511-9819-0025904B9B3C.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/72BACFBE-FFB7-E511-8D09-E03F49D6226B.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/88F43E31-00B8-E511-80A0-00E08148331D.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/8E7EDCB8-FFB7-E511-93D3-0025904C66A0.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/90FC24B9-FFB7-E511-A10F-0025905C4264.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/9221A3BE-FFB7-E511-AC22-BCAEC54E98EF.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/9C2DA4C0-FFB7-E511-9262-BCEE7B2FE09D.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/AE9CDFB8-FFB7-E511-BA19-0025904CDDFA.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/B47AA0B9-FFB7-E511-85E1-0025904C4E2A.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/B6B2B3E4-FFB7-E511-81CA-0025904C66A0.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/C23EE3B8-FFB7-E511-B39C-0025905C42B8.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/C2F021BE-FFB7-E511-8B31-F46D0450CEA0.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/D6C619BE-FFB7-E511-83D6-F46D043B3D41.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/D8B326B8-FFB7-E511-A8D7-0025904C66E4.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/EC2982B9-FFB7-E511-B6DF-0025905C2CE4.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/F80B92C0-FFB7-E511-99B3-BCEE7B2FE09D.root',
       '/store/mc/RunIIFall15MiniAODv2/WW_TuneCUETP8M1_13TeV-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/60000/FA383850-FFB7-E511-BDE9-0025905C42F2.root' ] );


secFiles.extend( [
               ] )


