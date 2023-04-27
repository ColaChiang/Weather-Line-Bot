# 建置操作步驟
### 下載Git  
https://git-scm.com/downloads  

<img src="https://user-images.githubusercontent.com/73519160/234651184-73739df1-aa2d-49bd-b4db-9a67d7a11437.png" width="50%" height="50%">  

### 創建一個Github帳號  
https://github.com/  

<img src="https://user-images.githubusercontent.com/73519160/234621680-8999deee-93b8-4497-b84a-3fba536209e9.png" width="50%" height="50%">  

### 下載Github Desktop  
https://desktop.github.com/  

<img src="https://user-images.githubusercontent.com/73519160/234650501-87fb94fa-c05b-4167-87d4-e85c756682d8.png" width="50%" height="50%"> 
<img src="https://user-images.githubusercontent.com/73519160/234833977-5e9470a9-c9e2-40d1-bb52-32cb0b312b6d.png" width="50%" height="50%"> 
<img src="https://user-images.githubusercontent.com/73519160/234835476-dbcb8175-95ba-4b91-bdf8-abb649be3f4d.png" width="50%" height="50%"> 

### Github Repository：存放 project 的地方
#### 建立repo  

<img src="https://user-images.githubusercontent.com/73519160/234649492-372e9067-4ae2-4f51-872f-2e4060f054fd.png" width="50%" height="50%"> 

---

### 設定個人資料
    git config --global user.name "xxxxx"  
###
    git config --global user.email xxxxxxx@example.com  
    
### 查看個人資料
#### 使用Git指令  

    git config user.name  
###
    git config user.email
    
<img src="https://user-images.githubusercontent.com/73519160/234643974-e82701e3-c14b-4b62-9ab6-71b29981a8de.png" width="50%" height="50%">  

#### 使用Github Desktop  
<img src="https://user-images.githubusercontent.com/73519160/234653262-db1e8915-2984-46c7-918e-40c02162ea2a.png" width="50%" height="50%">
<img src="https://user-images.githubusercontent.com/73519160/234653576-be74c2b1-8c84-4c48-ae22-45ac9347ae4a.png" width="50%" height="50%">  

### (initial)初始化repo

    git init

### 從遠端repo拉取回本地（同步）

    git pull

### 從遠端repo複製資料  
  
#### 使用Github Desktop

<img src="https://user-images.githubusercontent.com/73519160/234901083-bbdd5bb1-4150-47bd-b130-163aa0590445.png" width="50%" height="50%">  

#### 使用Git指令  
複製HTTP網址
<img src="https://user-images.githubusercontent.com/73519160/234902038-2b255a31-30bd-42d5-b550-889865ee8e44.png" width="50%" height="50%">

    git clone 貼上HTTP網址

### 顯示修改檔案清單 -s：僅會顯示已修改的檔案名稱

    git status

### git add .

    git add <檔案名稱>
    將子目錄裡的所有檔案註冊到索引裡

### git commit

    -a : 有修改的檔案(不包括新增的檔案)，將其加入索引並提交。
    -m : 提交訊息

### git push

    從本地推送到遠端
    git push origin master 本地master分支推一份到origin節點
    git push -u origin master 把預設remote都設成origin

### git rm

    remove

---

## 建立電腦端 New repo

### mkdir 建立新資料夾

    code . 開啟vscode

### git init 初始化 repo

### git add .

### git commit(電腦)

### 建立 Github new repo

### git remote add https://github.com/xxx

### git push 推到 github

---

