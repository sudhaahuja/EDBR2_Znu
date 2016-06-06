import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/5275795E-E227-E611-B722-7845C4FC370A.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/5E8F510B-E227-E611-BF4F-02163E013662.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/60E8272A-E227-E611-9397-B82A72E0BCA2.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/6EFBD1EB-E127-E611-A510-008CFA0F50F4.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/84CC24DF-E127-E611-AB3A-0CC47AA989C6.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/A42872D9-E127-E611-AD57-0025904C669C.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/C481790B-EE27-E611-B994-0CC47A1E0746.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/CAADAAE6-E127-E611-A876-0CC47A4C8E82.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/D24108DE-E127-E611-BCCA-24BE05CE2D41.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/D8E731E5-E127-E611-9122-0CC47A4D7640.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/D8F6B0DE-E127-E611-8B04-549F358EB762.root',
       '/store/mc/RunIIFall15MiniAODv2/BulkGravToZZToZhadZinv_narrow_M-1200_13TeV-madgraph/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/50000/F60EB4DC-E127-E611-A700-0090FAA57690.root' ] );


secFiles.extend( [
               ] )
