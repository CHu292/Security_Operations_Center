$duration = 60  # theo dõi trong 60 giây
$interval = 1

$times = @()
$counts = @()

for ($i = 0; $i -lt $duration; $i += $interval) {
    $now = Get-Date -Format "HH:mm:ss"
    $count = (Get-Process -Name "powershell" -ErrorAction SilentlyContinue).Count
    $times += $now
    $counts += $count
    Write-Host "${now}: $count"
    Start-Sleep -Seconds $interval
}

# Tạo dữ liệu kết quả
$results = for ($i = 0; $i -lt $times.Count; $i++) {
    [PSCustomObject]@{
        Time = $times[$i]
        Count = $counts[$i]
    }
}

# Lấy đường dẫn Desktop
$desktopPath = [Environment]::GetFolderPath("Desktop")
$csvPath = Join-Path $desktopPath "process_monitor.csv"

# Xuất file CSV lên Desktop
$results | Export-Csv -Path $csvPath -NoTypeInformation

Write-Host "`n File CSV đã được lưu tại: $csvPath"
