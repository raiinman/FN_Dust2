param([Parameter(Mandatory=$true)][string]$AreaId,
      [Parameter(Mandatory=$true)][string]$CaptureDirectory)
Add-Type -AssemblyName System.Drawing
$surveyDirectory = (Resolve-Path -LiteralPath $CaptureDirectory).Path
$tags = @('PY','NY','PX','NX','DOWN')
$sheet = [System.Drawing.Bitmap]::new(1920,780)
$graphics = [System.Drawing.Graphics]::FromImage($sheet)
$graphics.Clear([System.Drawing.Color]::FromArgb(28,28,28))
$font = [System.Drawing.Font]::new('Arial',13)
for($index=0;$index -lt $tags.Count;$index++) {
    $captureId = 'QA_'+$AreaId+'_G1_'+$tags[$index]+'_001'
    $sourcePath = Join-Path $surveyDirectory ($captureId+'.png')
    if(-not (Test-Path -LiteralPath $sourcePath)) { throw ('Missing capture '+$captureId) }
    $source = [System.Drawing.Image]::FromFile($sourcePath)
    $column = $index % 3
    $row = [Math]::Floor($index / 3)
    $left = $column * 640
    $top = $row * 390
    $graphics.DrawString($captureId,$font,[System.Drawing.Brushes]::White,$left+6,$top+3)
    $graphics.DrawImage($source,[System.Drawing.Rectangle]::new($left,$top+28,640,360))
    $source.Dispose()
}
$graphics.DrawString('Source-axis views; native floor-relative camera; pending review.',$font,[System.Drawing.Brushes]::White,1286,425)
$target = Join-Path $surveyDirectory ($AreaId+'_contact.png')
$sheet.Save($target,[System.Drawing.Imaging.ImageFormat]::Png)
$font.Dispose()
$graphics.Dispose()
$sheet.Dispose()
Write-Output $target
