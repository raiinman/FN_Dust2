param([Parameter(Mandatory=$true)][string]$CaptureDirectory,
      [Parameter(Mandatory=$true)][string]$PlanPath)
# Original-resolution JPEG derivatives of native captures; never synthesize pixels.
Add-Type -AssemblyName System.Drawing
$sourceDirectory=(Resolve-Path -LiteralPath $CaptureDirectory).Path
$plan=Get-Content -LiteralPath $PlanPath -Raw | ConvertFrom-Json
$folders=@{CTSPAWN='ct_spawn';CTMID='ct_mid';TOPMID='mid';LONGA='long_a';SHORT='short';UPTUN='upper_tunnels';LOWTUN='lower_tunnels';BSITE='b_site';SIDEPIT='side_pit';TSPAWN='t_spawn';ASITE='a_site'}
$encoder=[System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
$parameters=[System.Drawing.Imaging.EncoderParameters]::new(1)
$parameters.Param[0]=[System.Drawing.Imaging.EncoderParameter]::new([System.Drawing.Imaging.Encoder]::Quality,[long]94)
foreach($item in $plan.captures) {
    $source=Join-Path $sourceDirectory ($item.id+'.png')
    if(-not (Test-Path -LiteralPath $source)) { continue }
    $areaKey=$item.id.Split('_')[1]
    $destination=Join-Path $PSScriptRoot ('../reference/images/'+$folders[$areaKey]+'/'+$item.id+'.jpg')
    New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
    if(Test-Path -LiteralPath $destination) { continue }
    $bitmap=[System.Drawing.Image]::FromFile($source)
    if($bitmap.Width -ne 1280 -or $bitmap.Height -ne 720) { throw 'Unexpected capture resolution' }
    $bitmap.Save($destination,$encoder,$parameters)
    $bitmap.Dispose()
}
$parameters.Dispose()
Write-Output 'Prepared JPEG derivatives; visual acceptance is recorded separately.'
