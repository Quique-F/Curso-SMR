$miVariable = "Global"
function Invoke-AmbitoTest {
    $miVariable = "Local"
    Write-Host "Interno: $miVariable"
}
Invoke-AmbitoTest
