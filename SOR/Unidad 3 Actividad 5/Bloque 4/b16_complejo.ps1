$users =@{n="Ana"; e=20; r="Admin"}, @{n="Tom" ; e=15; r="User"}
foreach ($u in $users) {
    if ($u.e -ge 18 -and $u.r -eq "Admin") { "$($i.n) es Admin Mayor"}
}