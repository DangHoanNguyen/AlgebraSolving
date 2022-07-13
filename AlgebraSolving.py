import arrange
import boSungMatrix
import gauss

ls = [[1,1,-2],[2,3,-7],[5,2,1]]
hstd = [6,16,16]

ls = boSungMatrix.boSungMatrix(ls,hstd)
ls1 = arrange.arange(ls)
print(ls1)

# Cần chỉnh sửa số lần lặp lại arrange.arange() và gaus.Gauss()
ls1 = gauss.Gauss(ls1)
ls1 = arrange.arange(ls1)
ls1 = gauss.Gauss(ls1)
ls1 = arrange.arange(ls1)


print(ls1)