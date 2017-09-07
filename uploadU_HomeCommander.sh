now="$(date)"
sed -i "s/^Current date.*/Current date ${now}/" ./README.md
git add .
git commit -m "Automated Commit"
git push origin master
