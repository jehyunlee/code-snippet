### Function of example `bash` shell

* [chk_seq.sh]()
    ```bash
    #!/bin/bash
    
    SET=$(seq 0 25)
    for i in $SET
    do
      cp nohup_run.sh nohup_run_$i.sh
      sed -i "s/%/$i/" nohup_run_$i.sh
      nohup ./nohup_run_$i.sh > nohup_run_$i.out 2>&1&
    done
    ```
    
    (1) generate sequential array  
    ```bash
    $ SET=$(seq 0 25)  
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
    ```
    
    (2) `for` loop  
    ```bash
    for i in $SET
    do
      .......
    done
    ```
    
    (3) `cp`: copy files  
    ```bash
    cp nohup_run.sh nohup_run_$i.sh
    ```
    
    (4) `sed`: replace `%` with `$i` in file `nohup_run_$i.sh`   
    ```bash
    sed -i "s/%/$i/" nohup_run_$i.sh
    ```  
    * `-i` : inplace  
    * more options: [[Link](https://soooprmx.com/archives/8272)]
    
    (5) `nohup`: run 
    ```bash
    nohup ./nohup_run_$i.sh > nohup_run_$i.out 2>&1&
    ```
    * detailed explanation on `nohup` [[Link](https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_nohup_%EC%82%AC%EC%9A%A9%EB%B2%95)]
    * detailed explanation on `2>&1&` [[Link](https://reebok.tistory.com/56)]
    
