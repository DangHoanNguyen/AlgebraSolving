# array_khoi_tao duoc khoi tao trc chuong trinh
# array_hs_free gom cac he so tu do duoc nguoi dung nhap vao

def boSungMatrix(array_khoi_tao, array_hs_free):
    array_sau_bo_sung = array_khoi_tao
    for i in range(len(array_hs_free)):
        array_sau_bo_sung[i].append(array_hs_free[i])

    return array_sau_bo_sung