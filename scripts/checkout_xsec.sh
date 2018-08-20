# Source CMS environment
source /cvmfs/cms.cern.ch/cmsset_default.sh

# Get CMSSW release
cmsrel CMSSW_9_4_10
cd CMSSW_9_4_10/src
eval `scramv1 runtime -sh` # cmsenv

# GenXSec tools
git clone -b xsec https://github.com/ArturAkh/genproductions.git

cp genproductions/scripts/run_xsecs.sh .
mkdir ../../htcondor_results
mkdir ../../htcondor_results/error
mkdir ../../htcondor_results/log
mkdir ../../htcondor_results/out

cp genproductions/scripts/*.jdl genproductions/scripts/arguments.txt genproductions/scripts/run_xsecs.sh ../../htcondor_results/
