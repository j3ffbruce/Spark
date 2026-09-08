$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot"

$env:PATH = "$env:JAVA_HOME\bin;$PWD\.venv\Scripts;$env:PATH"

$env:PYSPARK_PYTHON = "$PWD\.venv\Scripts\python.exe"
$env:PYSPARK_DRIVER_PYTHON = "$PWD\.venv\Scripts\python.exe"

$env:SPARK_VERSION = "3.5"
$env:SPARK_HOME = $null

Write-Host "Setup Env is done!"
Write-Host "JAVA_HOME: $env:JAVA_HOME"
Write-Host "PYSPARK_PYTHON: $env:PYSPARK_PYTHON"
Write-Host "SPARK_VERSION: $env:SPARK_VERSION"