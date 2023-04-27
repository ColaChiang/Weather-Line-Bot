# 建置操作步驟

## 安裝設定
### 1. 下載Git <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="25px" height="25px">  
https://git-scm.com/downloads  

<img src="https://user-images.githubusercontent.com/73519160/234651184-73739df1-aa2d-49bd-b4db-9a67d7a11437.png" width="50%" height="50%">  

### 2. 創建一個Github帳號 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" width="25px" height="25px">  
https://github.com/  

<img src="https://user-images.githubusercontent.com/73519160/234621680-8999deee-93b8-4497-b84a-3fba536209e9.png" width="50%" height="50%">  

### 3. 下載Github Desktop <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/2048px-Github-desktop-logo-symbol.svg.png" width="30px" height="30px"> 
https://desktop.github.com/  

<img src="https://user-images.githubusercontent.com/73519160/234650501-87fb94fa-c05b-4167-87d4-e85c756682d8.png" width="50%" height="50%">  
✔安裝完後點擊sign in
<img src="https://user-images.githubusercontent.com/73519160/234833977-5e9470a9-c9e2-40d1-bb52-32cb0b312b6d.png" width="50%" height="50%"> 
✔登入後會帶出Github帳號，選擇Email後按Finish
<img src="https://user-images.githubusercontent.com/73519160/234835476-dbcb8175-95ba-4b91-bdf8-abb649be3f4d.png" width="50%" height="50%"> 

---

## Github 頁面
### 1. Github Repository：存放 project 的地方
#### 建立repository(repo) 儲存庫  

✔點選+號，按New repository  
<img src="https://user-images.githubusercontent.com/73519160/234649492-372e9067-4ae2-4f51-872f-2e4060f054fd.png" width="50%" height="50%"> 

✔設定repository  
<img src="https://user-images.githubusercontent.com/73519160/234906070-8906f2c7-2d22-4472-9f58-280e5555950e.png" width="50%" height="50%"> 

#### 欄位說明：
```
Repository name：儲存庫名稱(不得重複)
Description：專案的描述
設定權限：
1. Public(公開)：任何人都能看到
2. Private(私有)：只有你邀請的人可以看到
Add a README file：建議勾選，別人造訪你的儲存庫會看到的簡述，使用Markdown語法編輯
Add .gitignore(可忽略)：新增.gitignore文件，告訴Git在控管時要忽略那些檔案
Choose a license(可忽略)：程式碼授權條款
```

---

### 設定個人資料
#### <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="25px" height="25px"> 使用Git指令 
    git config --global user.name "xxxxx"  
###
    git config --global user.email xxxxxxx@example.com  
    
#### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/2048px-Github-desktop-logo-symbol.svg.png" width="30px" height="30px"> 使用Github Desktop(若安裝時有登入則不需設定)  
✔點選File的Options  
<img src="https://user-images.githubusercontent.com/73519160/234926594-b8d034ea-5305-4575-8d3d-7a5cd72fd690.png" width="50%" height="50%">  
✔點選Sign in  
<img src="https://user-images.githubusercontent.com/73519160/234926325-14b0136d-69f3-41be-ba20-5ef115b795f9.png" width="50%" height="50%"> 

### 查看個人資料
#### <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="25px" height="25px"> 使用Git指令  

    git config user.name  
###
    git config user.email
    

<img src="https://user-images.githubusercontent.com/73519160/234643974-e82701e3-c14b-4b62-9ab6-71b29981a8de.png" width="50%" height="50%">  

### 從遠端repository複製資料  
 
#### <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="25px" height="25px"> 使用Git指令  
✔複製HTTP網址  

<img src="https://user-images.githubusercontent.com/73519160/234902038-2b255a31-30bd-42d5-b550-889865ee8e44.png" width="50%" height="50%">
✔在cmd切換到要存放的目錄後輸入下面的指令  

    git clone 貼上HTTP網址  
    
#### <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/2048px-Github-desktop-logo-symbol.svg.png" width="30px" height="30px"> 使用Github Desktop  
✔點選Open With Github Desktop    
<img src="https://user-images.githubusercontent.com/73519160/234901083-bbdd5bb1-4150-47bd-b130-163aa0590445.png" width="50%" height="50%">  
✔選擇要複製的路徑，點選clone  
<img src="https://user-images.githubusercontent.com/73519160/234925362-e2122cc8-cb21-4582-a39b-e164717cac2d.png" width="50%" height="50%">  

    
---

### (initial)初始化repo

    git init

### 從遠端repo拉取回本地（同步）

    git pull


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

