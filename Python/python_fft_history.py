from sage import *

from pylab import *
fft(array([1, 2, 3, 5]))
A = fft(array([1, 2, 3, 5]))
A[:2] = 0
A
ifft(A)
A = fft(array([1, 2, 3, 5]))
A[2:] = 0
A
ifft(A)
plot(ifft(A))
plot(real(ifft(A)))
show()
matplotlib.use()
from pylab import *
A = randn(2, 2)
A
A = randn(4)
A
fft(A)
ifft(fft(A))
plot(A)
show()
matplotlib.use
matplotlib.use('cairo.pdf')
from matplotlib import use
matplotlib.use('cairo.pdf')
use('cairo.pdf')
A = randn(4)
from pylab import *
A = randn(5)
A
real(fft(A))
plot(A, real(fft(A)))


A = load('coeff.txt')
A = loadtxt('coeff.txt')

heavySide = array(range(-10, 11)) > 0
heavySide
heavySide+0
plot(heavySide)
clf()
plot(heavySide, convolve(heavySide, A))

heavySide = 0+(array(range(-100, 101)) > 0)
heavySide
convolve(heavySide, A)
plot(convolve(heavySide, A))
clf
plot(A)
A = loadtxt('coeff.txt')
plot(range(0, 42), A)
plot(range(0, 42), A)
A
A.shape
plot(range(0, 43), A)
xlabel('Zeit')
ylabel('Impulsantwort')
show()

legend('Koeffizienten des FIR (vermutlich Tiefpass)')

title('Koeffizienten des FIR (vermutlich Tiefpass)')

q
savefig('coeff.png')
s = array(range(-5, 6)) > 0
s
s += 0
s
s = s+0
s
plot(s)
plot(s, 'x')
h = array([0.65, 0.25, 0.1])
h
plot(convolve(s, h), 'og')
clf()
plot(convolve(s, h), 'g')
s = 0+(array(range(-5, 20)) > 0)
clf()
plot(convolve(s, h), 'g')
s

plot(convolve(s, h, 'same'), 'g')
plot(convolve(s, h, 'valid'), 'g')
clf()
plot(convolve(s, h, 'valid'), 'g')
plot(h)
clf()
plot(h)
plot(h, '.')
A = loadtxt('coeff.txt')
plot(abs(fft(A))
#plot(abs(fft(A))
#plot(A)
plot(abs(ifft(A)))
plot(abs(fftshift(fft(A))))
A = loadtxt('coeff.txt')
plot(abs(fftshift(fft(A))))
plot(abs(fftshift(fft(A))), range(*A.shape))
plot(range(*A.shape))
clf()
plot(range(*A.shape))
plot(range(*A.shape) - len(A)/2)
plot(range(*A.shape) - size(A)/2.0)
clf()

plot(abs(fftshift(fft(A))))
clf()
plot(abs(fftshift(fft(A))))
title('Magnitudenspektrum der Impulsantwort des Filters aus coeff.dat')
xlabel('Frequenz; kleine Frequenzen bei ~20, negative links davon, positive rechts (irgendwie lässt sich die Skalierung nicht einstellen?!)')
xlabel('Frequenz; kleine Frequenzen bei ~20, negative links davon, positive rechts')
ylabel('Betrag der Antwort')
savefig('fft.png')
A = loadtxt('coeff.txt')
plot(abs(fft(A)), range(*A.shape))
plot(abs(fft(A)))
clf()
plot(abs(fft(A)))
A
plot(A)
A = range(42, -1, -1)
A
A = A/42.0
A = array(A)
A
A = A/42.0
A
plot(A)
A.size
A.size = 100
B = zeros(100)
B[:43] = A
B
plot(B)
A = zeros(100) + array(range(10, -1, -1))/10
A = zeros(100) 
A += array(range(-10, -1, -1))/10
A[:10] += array(range(-10, -1, -1))/10
A[:11] += array(range(-10, -1, -1))/10
array(range(-10, -1, -1))/10
array(range(10, -1, -1))/10
A[:10] += array(range(10, -1, -1))/10
A[:11] += array(range(10, -1, -1))/10
A
A = zeros(100) 
A[:11] += array(range(10, -1, -1))/10.0
A
A[89:] += reversed(array(range(10, -1, -1))/10.0)
A = zeros(100) 
A[:3] += reversed(array(range(3, -1, -1))/3.0)
A[:3] += (array(range(3, -1, -1))/3.0)
A[:2] += (array(range(3, -1, -1))/3.0)
A[:4] += (array(range(3, -1, -1))/3.0)
A
plot(A)
reversed(A)

A + A[array(range(99, -1, -1))]
A = A + A[array(range(99, -1, -1))]
plot(A)
plot(ifft(A))
plot(fftshift(ifft(A)))
plot(A)
plot(ifft(A))
plot(fftshift(ifft(A)))
B = loadtxt('coeff.txt')
B
plot(B)
A = zeros(42) + array(range(6, -1, -1))/10
A = zeros(42)
A[:7] = array(range(6, -1, -1))/6.0
A
A[93:]
A[35:]
A = A + A[array(range(41, -1, -1))]
A
plot(A)
clf()
plot(A)
plot(ifft(A))
B = loadtxt('coeff.txt')
plot(B)
plot(A)
clf(); plot(fftshift(ifft(A)); plot(B)
clf(); plot(fftshift(ifft(A))); plot(B)
help savetxt
savetxt('unsere_coeffs.txt', fftshift(ifft(A)))
A = loadtxt('dump_file.dat')
plot(A)
A = loadtxt('dump_file.dat')
plot(A)
plot(loadtxt('sample.dat'))
A = (loadtxt('sample.dat'))
A
A.shape
plot(loadtxt('sample.dat'))
A = (loadtxt('dump_file.dat'))
A = ((loadtxt('dump_file.dat')))
A.shape
plot(fft(A))
plot(fftshift(fft(A)))
plot(fft(A))
A = loadtxt('dump_file.dat')
maximum(fft(A))
plot(fft(A))
max(fft(A))
max(abs(fft(A)))
plot(abs(fft(A)))
plot(angle(fft(A)))
