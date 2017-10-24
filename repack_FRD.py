import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import glob
import os

cmsswbase = os.path.expandvars("$CMSSW_BASE/")
inputPath = '/tmp/fff'

process = cms.Process("SRC")

process.load("DQM.SiStripCommon.MessageLogger_cfi")

process.FastMonitoringService = cms.Service("FastMonitoringService",
        sleepTime = cms.untracked.int32(1),
        microstateDefPath = cms.untracked.string( cmsswbase+'/src/EventFilter/Utilities/plugins/microstatedef.jsd'),
        fastMicrostateDefPath = cms.untracked.string( cmsswbase+'/src/EventFilter/Utilities/plugins/microstatedeffast.jsd'),
        fastName = cms.untracked.string( 'fastmoni' ),
        slowName = cms.untracked.string( 'slowmoni' )
)

process.EvFDaqDirector = cms.Service("EvFDaqDirector",
        runNumber = cms.untracked.uint32(000044),
        buBaseDir = cms.untracked.string(inputPath),
        directorIsBu = cms.untracked.bool(False),
        testModeNoBuilderUnit = cms.untracked.bool(False)
)

process.source = cms.Source("FedRawDataInputSource",
        runNumber = cms.untracked.uint32(000044),
        getLSFromFilename = cms.untracked.bool(True),
        testModeNoBuilderUnit = cms.untracked.bool(False),
        verifyAdler32 = cms.untracked.bool(True),
        verifyChecksum = cms.untracked.bool(True),
        useL1EventID = cms.untracked.bool(True),
        eventChunkSize = cms.untracked.uint32(16),
        numBuffers = cms.untracked.uint32(2),
        eventChunkBlock = cms.untracked.uint32(1),
        fileListMode = cms.untracked.bool(True),
        fileNames = cms.untracked.vstring()
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("run000044.root"),
  outputCommands = cms.untracked.vstring("drop *", "keep FEDRawDataCollection_*_*_*")
)

process.e = cms.EndPath(process.out)


fnames = glob.glob(inputPath+"/run"+"000044"+"/*ls000*.raw")
for f in fnames :
        process.source.fileNames.extend(cms.untracked.vstring('file:'+f))

