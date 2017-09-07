now="$(date)"
your_date=now
sed -i "s/^Current date.*/Current date ${your_date}/" /README.md
git add .
git commit -m "Automated Commit"
git push origin master
