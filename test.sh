
#!/bin/bash
email='axeprpr@gmail.com'
name='axeprpr'
git config --global user.email $email
git config --global user.name $name
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/"$name"/$REPLY.git
git push -u origin master
echo -ne "#!/bin/bash\ngit add .\n git commit -m "WTF?" \n git push origin master">>push.sh
chmod 777 push.sh
