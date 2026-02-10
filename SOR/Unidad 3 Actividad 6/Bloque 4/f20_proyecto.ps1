function New-Dir { New-Item -Path (Read-Host "Nombre") -ItemType Directory }
function Get-View { Get-ChildItem }

do {
    $op = Read-Host "1.Dir / 2.Ver / 3.Salir"
    if($op -eq "1"){ New-Dir }
    if($op -eq "2"){ Get-View }
} while ($op -ne "3")