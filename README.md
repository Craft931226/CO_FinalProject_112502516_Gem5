#  CO_FinalProject_Gem5
 所有數據stats and log都已附上
## (Q2) Enable L3 last level cache in GEM5 + NVMAIN (15%) ( 看到 log 裡面有 L3 cache 的資訊 )
### 修改檔案
* src/cpu/BaseCPU.py
* configs/common/CacheConfig.py
* configs/common/Options.py
* configs/common/Caches.py
* src/mem/Xbar.py
## (Q3) Config last level cache to  2-way and full-way associative cache and test performance (15%)
 必須跑benchmark quicksort在 2-way跟 full way (直接在 L3 cache implement，可以用 miss rate 判斷是否成功 )
* 僅指令不同，在 所有指令.txt 裡
## (Q4) Modify last level cache policy based on frequency based replacement policy (15%)
* 修改 configs/common/Caches.py/L3Cache 的replacement_policy
(假設系統使用LRURP)
## (Q5) Test the performance of write back and write through policy based on 4-way associative cache with isscc_pcm(15%) 
 必須跑benchmark multiply 在 write through 跟 write back ( gem5 default 使用 write back，可以用 write request 的數量判斷write through 是否成功 
* 修改 src/mem/cache/cache.cc and cache.hh 但未在數據成果有顯著差異
(應該是要修改base.cc)
## bonus X
