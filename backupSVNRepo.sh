if [ $# -lt 2 ];then
	echo "Usage:"
	echo "$0 svnrootPath backupToPath"
	exit 1
fi

svnrootPath=$1
backupToPath=$2
backupTime=`date +%Y%m%d%H%M%S`

repoNames="
	my_project_1
"
targetPath=$backupToPath"_"$backupTime
sudo mkdir -p $targetPath
for repoName in $repoNames;do
	echo "Backup $svnrootPath/$repoName -> $targetPath/$repoName"_"$backupTime"
	sudo svnadmin dump $svnrootPath/$repoName > $targetPath/$repoName"_"$backupTime
done

zipFileName=$targetPath/../myproject_dump"_"$backupTime.zip

sudo zip -r $zipFileName $targetPath/*

echo "Uploading"
scp $zipFileName usr@mydomain.win:~/my_home
rm -rf $zipFileName $targetPath
echo "Backup finish"
