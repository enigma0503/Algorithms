param([switch]$Elevated)

function Test-Admin {
    $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
    $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated) {
        # tried to elevate, did not work, aborting
    } else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
    }
    exit
}

'running with full privileges'

Update-HostStorageCache
foreach($disk in Get-Disk)
{
# Variable specifying the drive you want to extend
$drives=(Get-Partition -DiskNumber $disk.Number | where {$_.DriveLetter}).DriveLetter

# Script to get the partition sizes and then resize the volume
$drive_letter=""
foreach($drive in $drives){
$drive_letter=$drive
}
$size = (Get-PartitionSupportedSize -DriveLetter $drive_letter)
Resize-Partition -DriveLetter $drive_letter -Size $size.SizeMax
}

