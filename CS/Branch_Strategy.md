# 브랜치 전략

- 브랜치는 5개로 이루어져있음
- master: 현재 서비스 버전의 브랜치(라이브 서버)
- hotfix: 현재 서비스에 오류, 버그가 발생했을 때 수정하기 위한 브랜치
- release: 다음 버전 서비스의 브랜치
- develop: 버전 업그레이드를 위한 작업이 이루어지는 브랜치
- features: 각 기능을 개발하는 브랜치(여러 개의 브랜치에서 기능 개발이 이루어지고 최종적으로 develop에 merge<br>
<br>

### 신규 기능 개발

<img src="https://user-images.githubusercontent.com/83870423/169844240-c341203f-ac72-4855-aa4e-640365755e79.png"></img>

1. develop 브랜치로부터 본인이 신규 개발할 기능을 위한 feature 브랜치를 생성
2. feature 브랜치에서 기능을 완성하면 develop 브랜치에 merge

### 라이브 서버로 배포

<img src="https://user-images.githubusercontent.com/83870423/171669184-82c073aa-ba90-4e4d-9368-bf794279fe8a.png"></img>
