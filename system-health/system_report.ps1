# --- Systeminformationen ---
$HOSTNAME = $env:COMPUTERNAME
$DATE = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# --- CPU-Auslastung (aktueller Wert in %) ---
# Win32_Processor.LoadPercentage ist schnell und ohne Zusatzmodule
$cpuObjs = Get-CimInstance Win32_Processor
$CPU_LOAD = "{0:N2}" -f ((($cpuObjs | Measure-Object -Property LoadPercentage -Average).Average))

# --- RAM-Auslastung ---
$mem = Get-CimInstance Win32_OperatingSystem
$TOTAL_MEM_GB = [math]::Round($mem.TotalVisibleMemorySize / 1MB, 2)
$FREE_MEM_GB  = [math]::Round($mem.FreePhysicalMemory   / 1MB, 2)
$USED_MEM_GB  = $TOTAL_MEM_GB - $FREE_MEM_GB
$MEM_USAGE_PERCENT = "{0:N2}" -f (($USED_MEM_GB / $TOTAL_MEM_GB) * 100)

# --- Festplatten-Auslastung (Systemlaufwerk) ---
$systemDrive = $env:SystemDrive  # z.B. 'C:'
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$systemDrive'"
$DISK_USAGE_PERCENT = "{0:N2}" -f ((1 - ($disk.FreeSpace / $disk.Size)) * 100)

# --- Ausgabe-Helfer ---
function Print-Line($icon, $label, $value, [ConsoleColor]$labelColor = 'Green') {
    Write-Host $icon -NoNewLine
    Write-Host (" {0}" -f $label) -ForegroundColor $labelColor -NoNewLine
    Write-Host (" {0}" -f $value)
}

# --- Ausgabe ---
Write-Host "==========================================="
Write-Host "    SYSTEM HEALTH REPORT for " -NoNewLine
Write-Host $HOSTNAME -ForegroundColor Green
Write-Host "    " -NoNewLine
Write-Host $DATE -ForegroundColor Yellow
Write-Host "==========================================="
Write-Host ""
Print-Line "CPU-LOAD:"          ("{0} %" -f $CPU_LOAD)
Print-Line "RAM-USAGE:"      ("{0} %" -f $MEM_USAGE_PERCENT)
Print-Line ("SYSTEM-DRIVE ({0}):" -f $systemDrive) ("{0} % belegt" -f $DISK_USAGE_PERCENT)
Write-Host ""
Write-Host "==========================================="
