# Python-path calibration candidates

Values are first switch sizes (`n >= threshold`). No crossover is not a threshold.

| Function | Layout | Distribution | Decision | Status | First size | Candidate range |
|---|---|---|---|---|---:|---|
| cel | contiguous_f32 | near_boundary | rayon | inconclusive | — | — |
| cel | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| cel | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| cel | contiguous_f32 | uniform | rayon | inconclusive | — | — |
| cel | contiguous_f32 | uniform | rayon_detached | inconclusive | — | — |
| cel | contiguous_f32 | uniform | gil | no_crossover | — | — |
| cel | contiguous_f64 | near_boundary | rayon | crossover | 5121 | [4097, 5121] |
| cel | contiguous_f64 | near_boundary | rayon_detached | crossover | 5121 | [4097, 5121] |
| cel | contiguous_f64 | near_boundary | gil | no_crossover | — | — |
| cel | contiguous_f64 | uniform | rayon | crossover | 5121 | [4097, 5121] |
| cel | contiguous_f64 | uniform | rayon_detached | crossover | 5121 | [4097, 5121] |
| cel | contiguous_f64 | uniform | gil | inconclusive | — | — |
| cel | python_list | near_boundary | rayon | no_crossover | — | — |
| cel | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| cel | python_list | near_boundary | gil | no_crossover | — | — |
| cel | python_list | uniform | rayon | no_crossover | — | — |
| cel | python_list | uniform | rayon_detached | no_crossover | — | — |
| cel | python_list | uniform | gil | inconclusive | — | — |
| cel | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| cel | strided_f64 | near_boundary | rayon_detached | no_crossover | — | — |
| cel | strided_f64 | near_boundary | gil | no_crossover | — | — |
| cel | strided_f64 | uniform | rayon | no_crossover | — | — |
| cel | strided_f64 | uniform | rayon_detached | no_crossover | — | — |
| cel | strided_f64 | uniform | gil | no_crossover | — | — |
| cel1 | contiguous_f32 | near_boundary | rayon | no_crossover | — | — |
| cel1 | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| cel1 | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| cel1 | contiguous_f32 | uniform | rayon | crossover | 12287 | [10242, 12287] |
| cel1 | contiguous_f32 | uniform | rayon_detached | crossover | 12287 | [10242, 12287] |
| cel1 | contiguous_f32 | uniform | gil | no_crossover | — | — |
| cel1 | contiguous_f64 | near_boundary | rayon | crossover | 14336 | [12289, 14336] |
| cel1 | contiguous_f64 | near_boundary | rayon_detached | crossover | 12288 | [10242, 12288] |
| cel1 | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| cel1 | contiguous_f64 | uniform | rayon | crossover | 10241 | [8193, 10241] |
| cel1 | contiguous_f64 | uniform | rayon_detached | crossover | 12288 | [10242, 12288] |
| cel1 | contiguous_f64 | uniform | gil | no_crossover | — | — |
| cel1 | python_list | near_boundary | rayon | no_crossover | — | — |
| cel1 | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| cel1 | python_list | near_boundary | gil | no_crossover | — | — |
| cel1 | python_list | uniform | rayon | no_crossover | — | — |
| cel1 | python_list | uniform | rayon_detached | no_crossover | — | — |
| cel1 | python_list | uniform | gil | no_crossover | — | — |
| cel1 | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| cel1 | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| cel1 | strided_f64 | near_boundary | gil | no_crossover | — | — |
| cel1 | strided_f64 | uniform | rayon | inconclusive | — | — |
| cel1 | strided_f64 | uniform | rayon_detached | crossover | 12287 | [10242, 12287] |
| cel1 | strided_f64 | uniform | gil | no_crossover | — | — |
| cel2 | contiguous_f32 | near_boundary | rayon | inconclusive | — | — |
| cel2 | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| cel2 | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| cel2 | contiguous_f32 | uniform | rayon | crossover | 7167 | [6145, 7167] |
| cel2 | contiguous_f32 | uniform | rayon_detached | inconclusive | — | — |
| cel2 | contiguous_f32 | uniform | gil | no_crossover | — | — |
| cel2 | contiguous_f64 | near_boundary | rayon | crossover | 6144 | [5122, 6144] |
| cel2 | contiguous_f64 | near_boundary | rayon_detached | crossover | 5121 | [4097, 5121] |
| cel2 | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| cel2 | contiguous_f64 | uniform | rayon | crossover | 6144 | [5122, 6144] |
| cel2 | contiguous_f64 | uniform | rayon_detached | crossover | 7168 | [6145, 7168] |
| cel2 | contiguous_f64 | uniform | gil | inconclusive | — | — |
| cel2 | python_list | near_boundary | rayon | no_crossover | — | — |
| cel2 | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| cel2 | python_list | near_boundary | gil | no_crossover | — | — |
| cel2 | python_list | uniform | rayon | no_crossover | — | — |
| cel2 | python_list | uniform | rayon_detached | no_crossover | — | — |
| cel2 | python_list | uniform | gil | no_crossover | — | — |
| cel2 | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| cel2 | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| cel2 | strided_f64 | near_boundary | gil | no_crossover | — | — |
| cel2 | strided_f64 | uniform | rayon | inconclusive | — | — |
| cel2 | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| cel2 | strided_f64 | uniform | gil | no_crossover | — | — |
| cel3 | contiguous_f32 | near_boundary | rayon | inconclusive | — | — |
| cel3 | contiguous_f32 | near_boundary | rayon_detached | crossover | 5120 | [1, 5120] |
| cel3 | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| cel3 | contiguous_f32 | uniform | rayon | crossover | 6143 | [5122, 6143] |
| cel3 | contiguous_f32 | uniform | rayon_detached | crossover | 6143 | [5122, 6143] |
| cel3 | contiguous_f32 | uniform | gil | no_crossover | — | — |
| cel3 | contiguous_f64 | near_boundary | rayon | crossover | 6144 | [5122, 6144] |
| cel3 | contiguous_f64 | near_boundary | rayon_detached | crossover | 5121 | [4097, 5121] |
| cel3 | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| cel3 | contiguous_f64 | uniform | rayon | crossover | 5121 | [4097, 5121] |
| cel3 | contiguous_f64 | uniform | rayon_detached | crossover | 6144 | [5122, 6144] |
| cel3 | contiguous_f64 | uniform | gil | no_crossover | — | — |
| cel3 | python_list | near_boundary | rayon | no_crossover | — | — |
| cel3 | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| cel3 | python_list | near_boundary | gil | no_crossover | — | — |
| cel3 | python_list | uniform | rayon | no_crossover | — | — |
| cel3 | python_list | uniform | rayon_detached | no_crossover | — | — |
| cel3 | python_list | uniform | gil | no_crossover | — | — |
| cel3 | strided_f64 | near_boundary | rayon | crossover | 6143 | [5122, 6143] |
| cel3 | strided_f64 | near_boundary | rayon_detached | crossover | 6143 | [5122, 6143] |
| cel3 | strided_f64 | near_boundary | gil | no_crossover | — | — |
| cel3 | strided_f64 | uniform | rayon | crossover | 6143 | [5122, 6143] |
| cel3 | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| cel3 | strided_f64 | uniform | gil | no_crossover | — | — |
| el1 | contiguous_f32 | near_boundary | rayon | crossover | 3071 | [1, 3071] |
| el1 | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| el1 | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| el1 | contiguous_f32 | uniform | rayon | crossover | 3584 | [3584, 3584] |
| el1 | contiguous_f32 | uniform | rayon_detached | crossover | 3583 | [1, 3583] |
| el1 | contiguous_f32 | uniform | gil | no_crossover | — | — |
| el1 | contiguous_f64 | near_boundary | rayon | crossover | 3072 | [2562, 3072] |
| el1 | contiguous_f64 | near_boundary | rayon_detached | crossover | 3072 | [2562, 3072] |
| el1 | contiguous_f64 | near_boundary | gil | no_crossover | — | — |
| el1 | contiguous_f64 | uniform | rayon | crossover | 3584 | [3073, 3584] |
| el1 | contiguous_f64 | uniform | rayon_detached | crossover | 3584 | [3073, 3584] |
| el1 | contiguous_f64 | uniform | gil | no_crossover | — | — |
| el1 | python_list | near_boundary | rayon | no_crossover | — | — |
| el1 | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| el1 | python_list | near_boundary | gil | no_crossover | — | — |
| el1 | python_list | uniform | rayon | no_crossover | — | — |
| el1 | python_list | uniform | rayon_detached | no_crossover | — | — |
| el1 | python_list | uniform | gil | no_crossover | — | — |
| el1 | strided_f64 | near_boundary | rayon | crossover | 3071 | [1, 3071] |
| el1 | strided_f64 | near_boundary | rayon_detached | crossover | 3071 | [1, 3071] |
| el1 | strided_f64 | near_boundary | gil | no_crossover | — | — |
| el1 | strided_f64 | uniform | rayon | crossover | 3583 | [1, 3583] |
| el1 | strided_f64 | uniform | rayon_detached | crossover | 3583 | [1, 3583] |
| el1 | strided_f64 | uniform | gil | no_crossover | — | — |
| el2 | contiguous_f32 | near_boundary | rayon | crossover | 2047 | [1793, 2047] |
| el2 | contiguous_f32 | near_boundary | rayon_detached | crossover | 4096 | [2049, 4096] |
| el2 | contiguous_f32 | near_boundary | gil | inconclusive | — | — |
| el2 | contiguous_f32 | uniform | rayon | crossover | 2561 | [2561, 2561] |
| el2 | contiguous_f32 | uniform | rayon_detached | inconclusive | — | — |
| el2 | contiguous_f32 | uniform | gil | no_crossover | — | — |
| el2 | contiguous_f64 | near_boundary | rayon | crossover | 2048 | [1793, 2048] |
| el2 | contiguous_f64 | near_boundary | rayon_detached | crossover | 1792 | [1537, 1792] |
| el2 | contiguous_f64 | near_boundary | gil | crossover | 32768 | [28673, 32768] |
| el2 | contiguous_f64 | uniform | rayon | crossover | 2561 | [2049, 2561] |
| el2 | contiguous_f64 | uniform | rayon_detached | crossover | 2561 | [2049, 2561] |
| el2 | contiguous_f64 | uniform | gil | no_crossover | — | — |
| el2 | python_list | near_boundary | rayon | crossover | 32767 | [4097, 32767] |
| el2 | python_list | near_boundary | rayon_detached | crossover | 32767 | [4097, 32767] |
| el2 | python_list | near_boundary | gil | inconclusive | — | — |
| el2 | python_list | uniform | rayon | no_crossover | — | — |
| el2 | python_list | uniform | rayon_detached | no_crossover | — | — |
| el2 | python_list | uniform | gil | no_crossover | — | — |
| el2 | strided_f64 | near_boundary | rayon | crossover | 2048 | [2048, 2048] |
| el2 | strided_f64 | near_boundary | rayon_detached | crossover | 2048 | [2048, 2048] |
| el2 | strided_f64 | near_boundary | gil | inconclusive | — | — |
| el2 | strided_f64 | uniform | rayon | inconclusive | — | — |
| el2 | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| el2 | strided_f64 | uniform | gil | no_crossover | — | — |
| el3 | contiguous_f32 | near_boundary | rayon | crossover | 1024 | [1024, 1024] |
| el3 | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| el3 | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| el3 | contiguous_f32 | uniform | rayon | crossover | 1280 | [1, 1280] |
| el3 | contiguous_f32 | uniform | rayon_detached | crossover | 1280 | [1, 1280] |
| el3 | contiguous_f32 | uniform | gil | no_crossover | — | — |
| el3 | contiguous_f64 | near_boundary | rayon | crossover | 1024 | [897, 1024] |
| el3 | contiguous_f64 | near_boundary | rayon_detached | crossover | 1024 | [897, 1024] |
| el3 | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| el3 | contiguous_f64 | uniform | rayon | crossover | 1281 | [1025, 1281] |
| el3 | contiguous_f64 | uniform | rayon_detached | crossover | 1281 | [1025, 1281] |
| el3 | contiguous_f64 | uniform | gil | crossover | 4096 | [3585, 4096] |
| el3 | python_list | near_boundary | rayon | inconclusive | — | — |
| el3 | python_list | near_boundary | rayon_detached | inconclusive | — | — |
| el3 | python_list | near_boundary | gil | no_crossover | — | — |
| el3 | python_list | uniform | rayon | crossover | 4095 | [1537, 4095] |
| el3 | python_list | uniform | rayon_detached | crossover | 4095 | [1537, 4095] |
| el3 | python_list | uniform | gil | inconclusive | — | — |
| el3 | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| el3 | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| el3 | strided_f64 | near_boundary | gil | no_crossover | — | — |
| el3 | strided_f64 | uniform | rayon | crossover | 1280 | [1, 1280] |
| el3 | strided_f64 | uniform | rayon_detached | crossover | 1280 | [1, 1280] |
| el3 | strided_f64 | uniform | gil | no_crossover | — | — |
| ellipd | contiguous_f32 | near_boundary | rayon | crossover | 3584 | [3584, 3584] |
| ellipd | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| ellipd | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipd | contiguous_f32 | uniform | rayon | crossover | 5120 | [4097, 5120] |
| ellipd | contiguous_f32 | uniform | rayon_detached | crossover | 5120 | [4097, 5120] |
| ellipd | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellipd | contiguous_f64 | near_boundary | rayon | crossover | 3584 | [3073, 3584] |
| ellipd | contiguous_f64 | near_boundary | rayon_detached | crossover | 3584 | [3073, 3584] |
| ellipd | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellipd | contiguous_f64 | uniform | rayon | crossover | 4096 | [3585, 4096] |
| ellipd | contiguous_f64 | uniform | rayon_detached | crossover | 5121 | [4097, 5121] |
| ellipd | contiguous_f64 | uniform | gil | inconclusive | — | — |
| ellipd | python_list | near_boundary | rayon | no_crossover | — | — |
| ellipd | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| ellipd | python_list | near_boundary | gil | no_crossover | — | — |
| ellipd | python_list | uniform | rayon | inconclusive | — | — |
| ellipd | python_list | uniform | rayon_detached | no_crossover | — | — |
| ellipd | python_list | uniform | gil | no_crossover | — | — |
| ellipd | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| ellipd | strided_f64 | near_boundary | rayon_detached | crossover | 3583 | [1, 3583] |
| ellipd | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellipd | strided_f64 | uniform | rayon | crossover | 5120 | [4097, 5120] |
| ellipd | strided_f64 | uniform | rayon_detached | crossover | 5120 | [4097, 5120] |
| ellipd | strided_f64 | uniform | gil | no_crossover | — | — |
| ellipdinc | contiguous_f32 | near_boundary | rayon | crossover | 767 | [1, 767] |
| ellipdinc | contiguous_f32 | near_boundary | rayon_detached | crossover | 896 | [769, 896] |
| ellipdinc | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipdinc | contiguous_f32 | uniform | rayon | crossover | 2048 | [1025, 2048] |
| ellipdinc | contiguous_f32 | uniform | rayon_detached | crossover | 2048 | [1025, 2048] |
| ellipdinc | contiguous_f32 | uniform | gil | inconclusive | — | — |
| ellipdinc | contiguous_f64 | near_boundary | rayon | crossover | 768 | [642, 768] |
| ellipdinc | contiguous_f64 | near_boundary | rayon_detached | crossover | 768 | [642, 768] |
| ellipdinc | contiguous_f64 | near_boundary | gil | crossover | 4096 | [3585, 4096] |
| ellipdinc | contiguous_f64 | uniform | rayon | crossover | 1024 | [897, 1024] |
| ellipdinc | contiguous_f64 | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| ellipdinc | contiguous_f64 | uniform | gil | crossover | 4096 | [3585, 4096] |
| ellipdinc | python_list | near_boundary | rayon | crossover | 4095 | [897, 4095] |
| ellipdinc | python_list | near_boundary | rayon_detached | crossover | 4095 | [897, 4095] |
| ellipdinc | python_list | near_boundary | gil | no_crossover | — | — |
| ellipdinc | python_list | uniform | rayon | crossover | 2048 | [1025, 2048] |
| ellipdinc | python_list | uniform | rayon_detached | crossover | 2048 | [1025, 2048] |
| ellipdinc | python_list | uniform | gil | inconclusive | — | — |
| ellipdinc | strided_f64 | near_boundary | rayon | crossover | 896 | [769, 896] |
| ellipdinc | strided_f64 | near_boundary | rayon_detached | crossover | 767 | [1, 767] |
| ellipdinc | strided_f64 | near_boundary | gil | inconclusive | — | — |
| ellipdinc | strided_f64 | uniform | rayon | crossover | 1023 | [1, 1023] |
| ellipdinc | strided_f64 | uniform | rayon_detached | crossover | 2048 | [1025, 2048] |
| ellipdinc | strided_f64 | uniform | gil | inconclusive | — | — |
| ellipe | contiguous_f32 | near_boundary | rayon | crossover | 3583 | [1, 3583] |
| ellipe | contiguous_f32 | near_boundary | rayon_detached | crossover | 3583 | [1, 3583] |
| ellipe | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipe | contiguous_f32 | uniform | rayon | crossover | 14335 | [1, 14335] |
| ellipe | contiguous_f32 | uniform | rayon_detached | crossover | 14335 | [1, 14335] |
| ellipe | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellipe | contiguous_f64 | near_boundary | rayon | crossover | 3584 | [3073, 3584] |
| ellipe | contiguous_f64 | near_boundary | rayon_detached | crossover | 3584 | [3073, 3584] |
| ellipe | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellipe | contiguous_f64 | uniform | rayon | crossover | 14336 | [12289, 14336] |
| ellipe | contiguous_f64 | uniform | rayon_detached | crossover | 14336 | [12289, 14336] |
| ellipe | contiguous_f64 | uniform | gil | crossover | 32768 | [28673, 32768] |
| ellipe | python_list | near_boundary | rayon | no_crossover | — | — |
| ellipe | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| ellipe | python_list | near_boundary | gil | no_crossover | — | — |
| ellipe | python_list | uniform | rayon | inconclusive | — | — |
| ellipe | python_list | uniform | rayon_detached | inconclusive | — | — |
| ellipe | python_list | uniform | gil | inconclusive | — | — |
| ellipe | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| ellipe | strided_f64 | near_boundary | rayon_detached | crossover | 3583 | [1, 3583] |
| ellipe | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellipe | strided_f64 | uniform | rayon | crossover | 14336 | [14336, 14336] |
| ellipe | strided_f64 | uniform | rayon_detached | crossover | 14335 | [1, 14335] |
| ellipe | strided_f64 | uniform | gil | no_crossover | — | — |
| ellipeinc | contiguous_f32 | near_boundary | rayon | crossover | 767 | [642, 767] |
| ellipeinc | contiguous_f32 | near_boundary | rayon_detached | crossover | 767 | [642, 767] |
| ellipeinc | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipeinc | contiguous_f32 | uniform | rayon | crossover | 767 | [1, 767] |
| ellipeinc | contiguous_f32 | uniform | rayon_detached | crossover | 767 | [1, 767] |
| ellipeinc | contiguous_f32 | uniform | gil | crossover | 4095 | [1025, 4095] |
| ellipeinc | contiguous_f64 | near_boundary | rayon | crossover | 768 | [642, 768] |
| ellipeinc | contiguous_f64 | near_boundary | rayon_detached | crossover | 641 | [513, 641] |
| ellipeinc | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellipeinc | contiguous_f64 | uniform | rayon | crossover | 896 | [769, 896] |
| ellipeinc | contiguous_f64 | uniform | rayon_detached | crossover | 768 | [642, 768] |
| ellipeinc | contiguous_f64 | uniform | gil | crossover | 4096 | [3585, 4096] |
| ellipeinc | python_list | near_boundary | rayon | inconclusive | — | — |
| ellipeinc | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| ellipeinc | python_list | near_boundary | gil | no_crossover | — | — |
| ellipeinc | python_list | uniform | rayon | crossover | 1024 | [897, 1024] |
| ellipeinc | python_list | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| ellipeinc | python_list | uniform | gil | no_crossover | — | — |
| ellipeinc | strided_f64 | near_boundary | rayon | crossover | 768 | [768, 768] |
| ellipeinc | strided_f64 | near_boundary | rayon_detached | crossover | 768 | [768, 768] |
| ellipeinc | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellipeinc | strided_f64 | uniform | rayon | crossover | 768 | [768, 768] |
| ellipeinc | strided_f64 | uniform | rayon_detached | crossover | 768 | [768, 768] |
| ellipeinc | strided_f64 | uniform | gil | inconclusive | — | — |
| ellipf | contiguous_f32 | near_boundary | rayon | crossover | 1023 | [897, 1023] |
| ellipf | contiguous_f32 | near_boundary | rayon_detached | crossover | 1023 | [897, 1023] |
| ellipf | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipf | contiguous_f32 | uniform | rayon | inconclusive | — | — |
| ellipf | contiguous_f32 | uniform | rayon_detached | inconclusive | — | — |
| ellipf | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellipf | contiguous_f64 | near_boundary | rayon | crossover | 1024 | [897, 1024] |
| ellipf | contiguous_f64 | near_boundary | rayon_detached | crossover | 896 | [769, 896] |
| ellipf | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellipf | contiguous_f64 | uniform | rayon | crossover | 1024 | [897, 1024] |
| ellipf | contiguous_f64 | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| ellipf | contiguous_f64 | uniform | gil | inconclusive | — | — |
| ellipf | python_list | near_boundary | rayon | inconclusive | — | — |
| ellipf | python_list | near_boundary | rayon_detached | inconclusive | — | — |
| ellipf | python_list | near_boundary | gil | no_crossover | — | — |
| ellipf | python_list | uniform | rayon | inconclusive | — | — |
| ellipf | python_list | uniform | rayon_detached | no_crossover | — | — |
| ellipf | python_list | uniform | gil | no_crossover | — | — |
| ellipf | strided_f64 | near_boundary | rayon | crossover | 1023 | [897, 1023] |
| ellipf | strided_f64 | near_boundary | rayon_detached | crossover | 1024 | [1024, 1024] |
| ellipf | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellipf | strided_f64 | uniform | rayon | inconclusive | — | — |
| ellipf | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| ellipf | strided_f64 | uniform | gil | no_crossover | — | — |
| ellipk | contiguous_f32 | near_boundary | rayon | crossover | 8191 | [1, 8191] |
| ellipk | contiguous_f32 | near_boundary | rayon_detached | crossover | 8191 | [1, 8191] |
| ellipk | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipk | contiguous_f32 | uniform | rayon | crossover | 20480 | [1, 20480] |
| ellipk | contiguous_f32 | uniform | rayon_detached | crossover | 20480 | [1, 20480] |
| ellipk | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellipk | contiguous_f64 | near_boundary | rayon | crossover | 8192 | [7169, 8192] |
| ellipk | contiguous_f64 | near_boundary | rayon_detached | crossover | 8192 | [7169, 8192] |
| ellipk | contiguous_f64 | near_boundary | gil | no_crossover | — | — |
| ellipk | contiguous_f64 | uniform | rayon | crossover | 20481 | [16385, 20481] |
| ellipk | contiguous_f64 | uniform | rayon_detached | inconclusive | — | — |
| ellipk | contiguous_f64 | uniform | gil | inconclusive | — | — |
| ellipk | python_list | near_boundary | rayon | inconclusive | — | — |
| ellipk | python_list | near_boundary | rayon_detached | inconclusive | — | — |
| ellipk | python_list | near_boundary | gil | no_crossover | — | — |
| ellipk | python_list | uniform | rayon | no_crossover | — | — |
| ellipk | python_list | uniform | rayon_detached | no_crossover | — | — |
| ellipk | python_list | uniform | gil | no_crossover | — | — |
| ellipk | strided_f64 | near_boundary | rayon | crossover | 8191 | [1, 8191] |
| ellipk | strided_f64 | near_boundary | rayon_detached | crossover | 8191 | [1, 8191] |
| ellipk | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellipk | strided_f64 | uniform | rayon | crossover | 20480 | [1, 20480] |
| ellipk | strided_f64 | uniform | rayon_detached | crossover | 20480 | [1, 20480] |
| ellipk | strided_f64 | uniform | gil | no_crossover | — | — |
| ellipke | contiguous_f32 | near_boundary | rayon | crossover | 5120 | [4097, 5120] |
| ellipke | contiguous_f32 | near_boundary | rayon_detached | crossover | 5121 | [5121, 5121] |
| ellipke | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellipke | contiguous_f32 | uniform | rayon | crossover | 16383 | [12289, 16383] |
| ellipke | contiguous_f32 | uniform | rayon_detached | crossover | 16383 | [12289, 16383] |
| ellipke | contiguous_f32 | uniform | gil | inconclusive | — | — |
| ellipke | contiguous_f64 | near_boundary | rayon | crossover | 5121 | [4097, 5121] |
| ellipke | contiguous_f64 | near_boundary | rayon_detached | crossover | 4096 | [3585, 4096] |
| ellipke | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellipke | contiguous_f64 | uniform | rayon | crossover | 10241 | [8193, 10241] |
| ellipke | contiguous_f64 | uniform | rayon_detached | crossover | 16384 | [14337, 16384] |
| ellipke | contiguous_f64 | uniform | gil | crossover | 32768 | [28673, 32768] |
| ellipke | python_list | near_boundary | rayon | no_crossover | — | — |
| ellipke | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| ellipke | python_list | near_boundary | gil | no_crossover | — | — |
| ellipke | python_list | uniform | rayon | inconclusive | — | — |
| ellipke | python_list | uniform | rayon_detached | inconclusive | — | — |
| ellipke | python_list | uniform | gil | no_crossover | — | — |
| ellipke | strided_f64 | near_boundary | rayon | crossover | 5120 | [4097, 5120] |
| ellipke | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| ellipke | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellipke | strided_f64 | uniform | rayon | crossover | 20481 | [16385, 20481] |
| ellipke | strided_f64 | uniform | rayon_detached | crossover | 12288 | [10242, 12288] |
| ellipke | strided_f64 | uniform | gil | inconclusive | — | — |
| ellippi | contiguous_f32 | near_boundary | rayon | crossover | 511 | [1, 511] |
| ellippi | contiguous_f32 | near_boundary | rayon_detached | crossover | 511 | [1, 511] |
| ellippi | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellippi | contiguous_f32 | uniform | rayon | crossover | 640 | [1, 640] |
| ellippi | contiguous_f32 | uniform | rayon_detached | crossover | 640 | [1, 640] |
| ellippi | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellippi | contiguous_f64 | near_boundary | rayon | crossover | 512 | [449, 512] |
| ellippi | contiguous_f64 | near_boundary | rayon_detached | crossover | 512 | [449, 512] |
| ellippi | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellippi | contiguous_f64 | uniform | rayon | crossover | 641 | [513, 641] |
| ellippi | contiguous_f64 | uniform | rayon_detached | crossover | 768 | [642, 768] |
| ellippi | contiguous_f64 | uniform | gil | inconclusive | — | — |
| ellippi | python_list | near_boundary | rayon | inconclusive | — | — |
| ellippi | python_list | near_boundary | rayon_detached | inconclusive | — | — |
| ellippi | python_list | near_boundary | gil | no_crossover | — | — |
| ellippi | python_list | uniform | rayon | inconclusive | — | — |
| ellippi | python_list | uniform | rayon_detached | inconclusive | — | — |
| ellippi | python_list | uniform | gil | no_crossover | — | — |
| ellippi | strided_f64 | near_boundary | rayon | crossover | 511 | [1, 511] |
| ellippi | strided_f64 | near_boundary | rayon_detached | crossover | 511 | [1, 511] |
| ellippi | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellippi | strided_f64 | uniform | rayon | crossover | 640 | [1, 640] |
| ellippi | strided_f64 | uniform | rayon_detached | crossover | 640 | [1, 640] |
| ellippi | strided_f64 | uniform | gil | no_crossover | — | — |
| ellippiinc | contiguous_f32 | near_boundary | rayon | crossover | 383 | [1, 383] |
| ellippiinc | contiguous_f32 | near_boundary | rayon_detached | crossover | 383 | [1, 383] |
| ellippiinc | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellippiinc | contiguous_f32 | uniform | rayon | crossover | 640 | [1, 640] |
| ellippiinc | contiguous_f32 | uniform | rayon_detached | inconclusive | — | — |
| ellippiinc | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellippiinc | contiguous_f64 | near_boundary | rayon | crossover | 384 | [322, 384] |
| ellippiinc | contiguous_f64 | near_boundary | rayon_detached | crossover | 384 | [322, 384] |
| ellippiinc | contiguous_f64 | near_boundary | gil | crossover | 32768 | [28673, 32768] |
| ellippiinc | contiguous_f64 | uniform | rayon | crossover | 641 | [513, 641] |
| ellippiinc | contiguous_f64 | uniform | rayon_detached | crossover | 641 | [513, 641] |
| ellippiinc | contiguous_f64 | uniform | gil | inconclusive | — | — |
| ellippiinc | python_list | near_boundary | rayon | crossover | 32767 | [449, 32767] |
| ellippiinc | python_list | near_boundary | rayon_detached | crossover | 32767 | [449, 32767] |
| ellippiinc | python_list | near_boundary | gil | inconclusive | — | — |
| ellippiinc | python_list | uniform | rayon | inconclusive | — | — |
| ellippiinc | python_list | uniform | rayon_detached | no_crossover | — | — |
| ellippiinc | python_list | uniform | gil | no_crossover | — | — |
| ellippiinc | strided_f64 | near_boundary | rayon | crossover | 384 | [384, 384] |
| ellippiinc | strided_f64 | near_boundary | rayon_detached | crossover | 448 | [385, 448] |
| ellippiinc | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellippiinc | strided_f64 | uniform | rayon | crossover | 640 | [1, 640] |
| ellippiinc | strided_f64 | uniform | rayon_detached | crossover | 640 | [1, 640] |
| ellippiinc | strided_f64 | uniform | gil | no_crossover | — | — |
| ellippiinc_bulirsch | contiguous_f32 | near_boundary | rayon | crossover | 768 | [768, 768] |
| ellippiinc_bulirsch | contiguous_f32 | near_boundary | rayon_detached | crossover | 767 | [1, 767] |
| ellippiinc_bulirsch | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| ellippiinc_bulirsch | contiguous_f32 | uniform | rayon | inconclusive | — | — |
| ellippiinc_bulirsch | contiguous_f32 | uniform | rayon_detached | crossover | 1023 | [1, 1023] |
| ellippiinc_bulirsch | contiguous_f32 | uniform | gil | no_crossover | — | — |
| ellippiinc_bulirsch | contiguous_f64 | near_boundary | rayon | crossover | 768 | [642, 768] |
| ellippiinc_bulirsch | contiguous_f64 | near_boundary | rayon_detached | crossover | 768 | [642, 768] |
| ellippiinc_bulirsch | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| ellippiinc_bulirsch | contiguous_f64 | uniform | rayon | crossover | 1024 | [897, 1024] |
| ellippiinc_bulirsch | contiguous_f64 | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| ellippiinc_bulirsch | contiguous_f64 | uniform | gil | inconclusive | — | — |
| ellippiinc_bulirsch | python_list | near_boundary | rayon | no_crossover | — | — |
| ellippiinc_bulirsch | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| ellippiinc_bulirsch | python_list | near_boundary | gil | no_crossover | — | — |
| ellippiinc_bulirsch | python_list | uniform | rayon | inconclusive | — | — |
| ellippiinc_bulirsch | python_list | uniform | rayon_detached | inconclusive | — | — |
| ellippiinc_bulirsch | python_list | uniform | gil | no_crossover | — | — |
| ellippiinc_bulirsch | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| ellippiinc_bulirsch | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| ellippiinc_bulirsch | strided_f64 | near_boundary | gil | no_crossover | — | — |
| ellippiinc_bulirsch | strided_f64 | uniform | rayon | inconclusive | — | — |
| ellippiinc_bulirsch | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| ellippiinc_bulirsch | strided_f64 | uniform | gil | no_crossover | — | — |
| elliprc | contiguous_f32 | near_boundary | rayon | crossover | 8191 | [1, 8191] |
| elliprc | contiguous_f32 | near_boundary | rayon_detached | crossover | 8191 | [1, 8191] |
| elliprc | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| elliprc | contiguous_f32 | uniform | rayon | crossover | 6144 | [6144, 6144] |
| elliprc | contiguous_f32 | uniform | rayon_detached | inconclusive | — | — |
| elliprc | contiguous_f32 | uniform | gil | no_crossover | — | — |
| elliprc | contiguous_f64 | near_boundary | rayon | crossover | 8192 | [7169, 8192] |
| elliprc | contiguous_f64 | near_boundary | rayon_detached | crossover | 8192 | [7169, 8192] |
| elliprc | contiguous_f64 | near_boundary | gil | no_crossover | — | — |
| elliprc | contiguous_f64 | uniform | rayon | crossover | 6144 | [5122, 6144] |
| elliprc | contiguous_f64 | uniform | rayon_detached | crossover | 6144 | [5122, 6144] |
| elliprc | contiguous_f64 | uniform | gil | no_crossover | — | — |
| elliprc | python_list | near_boundary | rayon | no_crossover | — | — |
| elliprc | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| elliprc | python_list | near_boundary | gil | no_crossover | — | — |
| elliprc | python_list | uniform | rayon | no_crossover | — | — |
| elliprc | python_list | uniform | rayon_detached | no_crossover | — | — |
| elliprc | python_list | uniform | gil | no_crossover | — | — |
| elliprc | strided_f64 | near_boundary | rayon | crossover | 8191 | [1, 8191] |
| elliprc | strided_f64 | near_boundary | rayon_detached | crossover | 8191 | [1, 8191] |
| elliprc | strided_f64 | near_boundary | gil | no_crossover | — | — |
| elliprc | strided_f64 | uniform | rayon | inconclusive | — | — |
| elliprc | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| elliprc | strided_f64 | uniform | gil | no_crossover | — | — |
| elliprd | contiguous_f32 | near_boundary | rayon | inconclusive | — | — |
| elliprd | contiguous_f32 | near_boundary | rayon_detached | crossover | 1792 | [1792, 1792] |
| elliprd | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| elliprd | contiguous_f32 | uniform | rayon | inconclusive | — | — |
| elliprd | contiguous_f32 | uniform | rayon_detached | crossover | 1791 | [1, 1791] |
| elliprd | contiguous_f32 | uniform | gil | no_crossover | — | — |
| elliprd | contiguous_f64 | near_boundary | rayon | crossover | 1792 | [1537, 1792] |
| elliprd | contiguous_f64 | near_boundary | rayon_detached | crossover | 1792 | [1537, 1792] |
| elliprd | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| elliprd | contiguous_f64 | uniform | rayon | crossover | 1792 | [1537, 1792] |
| elliprd | contiguous_f64 | uniform | rayon_detached | crossover | 1792 | [1537, 1792] |
| elliprd | contiguous_f64 | uniform | gil | inconclusive | — | — |
| elliprd | python_list | near_boundary | rayon | no_crossover | — | — |
| elliprd | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| elliprd | python_list | near_boundary | gil | no_crossover | — | — |
| elliprd | python_list | uniform | rayon | no_crossover | — | — |
| elliprd | python_list | uniform | rayon_detached | no_crossover | — | — |
| elliprd | python_list | uniform | gil | no_crossover | — | — |
| elliprd | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| elliprd | strided_f64 | near_boundary | rayon_detached | crossover | 1791 | [1, 1791] |
| elliprd | strided_f64 | near_boundary | gil | no_crossover | — | — |
| elliprd | strided_f64 | uniform | rayon | inconclusive | — | — |
| elliprd | strided_f64 | uniform | rayon_detached | inconclusive | — | — |
| elliprd | strided_f64 | uniform | gil | no_crossover | — | — |
| elliprf | contiguous_f32 | near_boundary | rayon | crossover | 2047 | [1793, 2047] |
| elliprf | contiguous_f32 | near_boundary | rayon_detached | crossover | 2048 | [2048, 2048] |
| elliprf | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| elliprf | contiguous_f32 | uniform | rayon | crossover | 2047 | [1793, 2047] |
| elliprf | contiguous_f32 | uniform | rayon_detached | crossover | 2048 | [2048, 2048] |
| elliprf | contiguous_f32 | uniform | gil | no_crossover | — | — |
| elliprf | contiguous_f64 | near_boundary | rayon | crossover | 2048 | [1793, 2048] |
| elliprf | contiguous_f64 | near_boundary | rayon_detached | crossover | 1792 | [1537, 1792] |
| elliprf | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| elliprf | contiguous_f64 | uniform | rayon | crossover | 2048 | [1793, 2048] |
| elliprf | contiguous_f64 | uniform | rayon_detached | crossover | 1792 | [1537, 1792] |
| elliprf | contiguous_f64 | uniform | gil | inconclusive | — | — |
| elliprf | python_list | near_boundary | rayon | no_crossover | — | — |
| elliprf | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| elliprf | python_list | near_boundary | gil | no_crossover | — | — |
| elliprf | python_list | uniform | rayon | no_crossover | — | — |
| elliprf | python_list | uniform | rayon_detached | no_crossover | — | — |
| elliprf | python_list | uniform | gil | no_crossover | — | — |
| elliprf | strided_f64 | near_boundary | rayon | crossover | 2047 | [1793, 2047] |
| elliprf | strided_f64 | near_boundary | rayon_detached | crossover | 2048 | [2048, 2048] |
| elliprf | strided_f64 | near_boundary | gil | no_crossover | — | — |
| elliprf | strided_f64 | uniform | rayon | inconclusive | — | — |
| elliprf | strided_f64 | uniform | rayon_detached | crossover | 2048 | [2048, 2048] |
| elliprf | strided_f64 | uniform | gil | no_crossover | — | — |
| elliprg | contiguous_f32 | near_boundary | rayon | inconclusive | — | — |
| elliprg | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| elliprg | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| elliprg | contiguous_f32 | uniform | rayon | crossover | 1024 | [897, 1024] |
| elliprg | contiguous_f32 | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| elliprg | contiguous_f32 | uniform | gil | no_crossover | — | — |
| elliprg | contiguous_f64 | near_boundary | rayon | crossover | 896 | [769, 896] |
| elliprg | contiguous_f64 | near_boundary | rayon_detached | crossover | 896 | [769, 896] |
| elliprg | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| elliprg | contiguous_f64 | uniform | rayon | crossover | 896 | [769, 896] |
| elliprg | contiguous_f64 | uniform | rayon_detached | crossover | 896 | [769, 896] |
| elliprg | contiguous_f64 | uniform | gil | crossover | 4096 | [3585, 4096] |
| elliprg | python_list | near_boundary | rayon | no_crossover | — | — |
| elliprg | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| elliprg | python_list | near_boundary | gil | no_crossover | — | — |
| elliprg | python_list | uniform | rayon | crossover | 4095 | [1025, 4095] |
| elliprg | python_list | uniform | rayon_detached | crossover | 4095 | [1025, 4095] |
| elliprg | python_list | uniform | gil | crossover | 4096 | [4096, 4096] |
| elliprg | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| elliprg | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| elliprg | strided_f64 | near_boundary | gil | no_crossover | — | — |
| elliprg | strided_f64 | uniform | rayon | crossover | 4095 | [1025, 4095] |
| elliprg | strided_f64 | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| elliprg | strided_f64 | uniform | gil | crossover | 4096 | [4096, 4096] |
| elliprj | contiguous_f32 | near_boundary | rayon | crossover | 1023 | [1, 1023] |
| elliprj | contiguous_f32 | near_boundary | rayon_detached | crossover | 1023 | [1, 1023] |
| elliprj | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| elliprj | contiguous_f32 | uniform | rayon | crossover | 1024 | [1024, 1024] |
| elliprj | contiguous_f32 | uniform | rayon_detached | crossover | 1023 | [897, 1023] |
| elliprj | contiguous_f32 | uniform | gil | no_crossover | — | — |
| elliprj | contiguous_f64 | near_boundary | rayon | crossover | 1024 | [897, 1024] |
| elliprj | contiguous_f64 | near_boundary | rayon_detached | crossover | 1024 | [897, 1024] |
| elliprj | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| elliprj | contiguous_f64 | uniform | rayon | crossover | 768 | [642, 768] |
| elliprj | contiguous_f64 | uniform | rayon_detached | crossover | 1024 | [897, 1024] |
| elliprj | contiguous_f64 | uniform | gil | inconclusive | — | — |
| elliprj | python_list | near_boundary | rayon | inconclusive | — | — |
| elliprj | python_list | near_boundary | rayon_detached | inconclusive | — | — |
| elliprj | python_list | near_boundary | gil | no_crossover | — | — |
| elliprj | python_list | uniform | rayon | inconclusive | — | — |
| elliprj | python_list | uniform | rayon_detached | inconclusive | — | — |
| elliprj | python_list | uniform | gil | no_crossover | — | — |
| elliprj | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| elliprj | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| elliprj | strided_f64 | near_boundary | gil | no_crossover | — | — |
| elliprj | strided_f64 | uniform | rayon | crossover | 1023 | [897, 1023] |
| elliprj | strided_f64 | uniform | rayon_detached | crossover | 1023 | [897, 1023] |
| elliprj | strided_f64 | uniform | gil | no_crossover | — | — |
| heuman_lambda | contiguous_f32 | near_boundary | rayon | crossover | 383 | [1, 383] |
| heuman_lambda | contiguous_f32 | near_boundary | rayon_detached | inconclusive | — | — |
| heuman_lambda | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| heuman_lambda | contiguous_f32 | uniform | rayon | crossover | 320 | [1, 320] |
| heuman_lambda | contiguous_f32 | uniform | rayon_detached | crossover | 321 | [321, 321] |
| heuman_lambda | contiguous_f32 | uniform | gil | no_crossover | — | — |
| heuman_lambda | contiguous_f64 | near_boundary | rayon | crossover | 384 | [322, 384] |
| heuman_lambda | contiguous_f64 | near_boundary | rayon_detached | crossover | 384 | [322, 384] |
| heuman_lambda | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| heuman_lambda | contiguous_f64 | uniform | rayon | crossover | 321 | [257, 321] |
| heuman_lambda | contiguous_f64 | uniform | rayon_detached | crossover | 321 | [257, 321] |
| heuman_lambda | contiguous_f64 | uniform | gil | inconclusive | — | — |
| heuman_lambda | python_list | near_boundary | rayon | inconclusive | — | — |
| heuman_lambda | python_list | near_boundary | rayon_detached | inconclusive | — | — |
| heuman_lambda | python_list | near_boundary | gil | no_crossover | — | — |
| heuman_lambda | python_list | uniform | rayon | inconclusive | — | — |
| heuman_lambda | python_list | uniform | rayon_detached | inconclusive | — | — |
| heuman_lambda | python_list | uniform | gil | no_crossover | — | — |
| heuman_lambda | strided_f64 | near_boundary | rayon | crossover | 383 | [1, 383] |
| heuman_lambda | strided_f64 | near_boundary | rayon_detached | crossover | 383 | [1, 383] |
| heuman_lambda | strided_f64 | near_boundary | gil | no_crossover | — | — |
| heuman_lambda | strided_f64 | uniform | rayon | crossover | 320 | [1, 320] |
| heuman_lambda | strided_f64 | uniform | rayon_detached | crossover | 320 | [1, 320] |
| heuman_lambda | strided_f64 | uniform | gil | no_crossover | — | — |
| jacobi_zeta | contiguous_f32 | near_boundary | rayon | crossover | 448 | [448, 448] |
| jacobi_zeta | contiguous_f32 | near_boundary | rayon_detached | crossover | 448 | [448, 448] |
| jacobi_zeta | contiguous_f32 | near_boundary | gil | no_crossover | — | — |
| jacobi_zeta | contiguous_f32 | uniform | rayon | crossover | 640 | [1, 640] |
| jacobi_zeta | contiguous_f32 | uniform | rayon_detached | crossover | 640 | [1, 640] |
| jacobi_zeta | contiguous_f32 | uniform | gil | no_crossover | — | — |
| jacobi_zeta | contiguous_f64 | near_boundary | rayon | crossover | 448 | [385, 448] |
| jacobi_zeta | contiguous_f64 | near_boundary | rayon_detached | crossover | 448 | [385, 448] |
| jacobi_zeta | contiguous_f64 | near_boundary | gil | inconclusive | — | — |
| jacobi_zeta | contiguous_f64 | uniform | rayon | crossover | 768 | [642, 768] |
| jacobi_zeta | contiguous_f64 | uniform | rayon_detached | crossover | 641 | [513, 641] |
| jacobi_zeta | contiguous_f64 | uniform | gil | inconclusive | — | — |
| jacobi_zeta | python_list | near_boundary | rayon | no_crossover | — | — |
| jacobi_zeta | python_list | near_boundary | rayon_detached | no_crossover | — | — |
| jacobi_zeta | python_list | near_boundary | gil | no_crossover | — | — |
| jacobi_zeta | python_list | uniform | rayon | inconclusive | — | — |
| jacobi_zeta | python_list | uniform | rayon_detached | inconclusive | — | — |
| jacobi_zeta | python_list | uniform | gil | no_crossover | — | — |
| jacobi_zeta | strided_f64 | near_boundary | rayon | inconclusive | — | — |
| jacobi_zeta | strided_f64 | near_boundary | rayon_detached | inconclusive | — | — |
| jacobi_zeta | strided_f64 | near_boundary | gil | no_crossover | — | — |
| jacobi_zeta | strided_f64 | uniform | rayon | crossover | 640 | [1, 640] |
| jacobi_zeta | strided_f64 | uniform | rayon_detached | crossover | 640 | [1, 640] |
| jacobi_zeta | strided_f64 | uniform | gil | no_crossover | — | — |
