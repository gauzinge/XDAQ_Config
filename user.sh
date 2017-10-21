export JAVA_HOME=/usr/java/jdk1.8.0_151 
export CATALINA_HOME=/usr/local/apache-tomcat-8.0.22

## RCMS
export ANT_HOME=/opt/apache-ant-1.6.5
export RCMS_HOME=/opt/TriDAS/RunControl
export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$CATALINA_HOME:$PATH

#############################################################################
# Aliases
#############################################################################
alias  StartTomcat="$CATALINA_HOME/bin/startup.sh"
alias  StopTomcat="$CATALINA_HOME/bin/shutdown.sh"
alias  RunManager="java -jar ~/XDAQ_Config/manager.jar"
