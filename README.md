# opencv-face-detection
preprocessing of image for face recognition  
猫顔犬顔判定のための学習データ処理。与えられた画像から「人間の顔」「猫の顔」をきりとる処理。これらともにOpenCVにある学習済みモデルをそのまま利用。
しかし精度は非常に低く、「犬」に関してはOpenCVに学習済み重みがないため自分で学習する必要がある
