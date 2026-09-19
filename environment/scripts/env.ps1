$projectRoot = (Resolve-Path "$PSScriptRoot\..\..").Path
$venvPath = "$projectRoot\.venv"

$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot"
$env:HADOOP_HOME = "C:\hadoop-3.3.5"

$env:PATH = "$env:JAVA_HOME\bin;$env:HADOOP_HOME\bin;$venvPath\Scripts;$env:PATH"

$env:PYSPARK_PYTHON = "$venvPath\Scripts\python.exe"
$env:PYSPARK_DRIVER_PYTHON = "$venvPath\Scripts\python.exe"

$env:SPARK_VERSION = "3.5"
$env:SPARK_HOME = $null

Write-Host "ENVIROMENT OUTPUTS"
Write-Host "JAVA_HOME: $env:JAVA_HOME"
Write-Host "HADOOP_HOME: $env:HADOOP_HOME"
Write-Host "PYSPARK_PYTHON: $env:PYSPARK_PYTHON"
Write-Host "SPARK_VERSION: $env:SPARK_VERSION"