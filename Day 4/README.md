Day 4

* Randomisation (Mersenne Twister)
* Lists - basics



For a w-bit word length, the Mersenne Twister generates integers in the range [0, 2w−1].

The Mersenne Twister algorithm is based on a matrix linear recurrence over a finite binary field F2. The algorithm is a twisted generalised feedback shift register[52] (twisted GFSR, or TGFSR) of rational normal form (TGFSR(R)), with state bit reflection and tempering. The basic idea is to define a series xi through a simple recurrence relation, and then output numbers of the form xiT, where T is an invertible F2-matrix called a tempering matrix.

The general algorithm is characterized by the following quantities (some of these explanations make sense only after reading the rest of the algorithm):

w: word size (in number of bits)
n: degree of recurrence
m: middle word, an offset used in the recurrence relation defining the series x, 1 ≤ m < n
r: separation point of one word, or the number of bits of the lower bitmask, 0 ≤ r ≤ w − 1
a: coefficients of the rational normal form twist matrix
b, c: TGFSR(R) tempering bitmasks
s, t: TGFSR(R) tempering bit shifts
u, d, l: additional Mersenne Twister tempering bit shifts/masks
with the restriction that 2nw−r − 1 is a Mersenne prime. This choice simplifies the primitivity test and k-distribution test that are needed in the parameter search.

The series x is defined as a series of w-bit quantities with the recurrence relation:

{\displaystyle x_{k+n}:=x_{k+m}\oplus \left(({x_{k}}^{u}\mid {x_{k+1}}^{l})A\right)\qquad \qquad k=0,1,\ldots }{\displaystyle x_{k+n}:=x_{k+m}\oplus \left(({x_{k}}^{u}\mid {x_{k+1}}^{l})A\right)\qquad \qquad k=0,1,\ldots }
where {\displaystyle \mid }\mid  denotes concatenation of bit vectors (with upper bits on the left), ⊕ the bitwise exclusive or (XOR), xku means the upper w − r bits of xk, and xk+1l means the lower r bits of xk+1. The twist transformation A is defined in rational normal form as:

{\displaystyle A={\begin{pmatrix}0&I_{w-1}\\a_{w-1}&(a_{w-2},\ldots ,a_{0})\end{pmatrix}}}{\displaystyle A={\begin{pmatrix}0&I_{w-1}\\a_{w-1}&(a_{w-2},\ldots ,a_{0})\end{pmatrix}}}
with Iw−1 as the (w − 1) × (w − 1) identity matrix. The rational normal form has the benefit that multiplication by A can be efficiently expressed as: (remember that here matrix multiplication is being done in F2, and therefore bitwise XOR takes the place of addition)

{\displaystyle {\boldsymbol {x}}A={\begin{cases}{\boldsymbol {x}}\gg 1&x_{0}=0\\({\boldsymbol {x}}\gg 1)\oplus {\boldsymbol {a}}&x_{0}=1\end{cases}}}{\displaystyle {\boldsymbol {x}}A={\begin{cases}{\boldsymbol {x}}\gg 1&x_{0}=0\\({\boldsymbol {x}}\gg 1)\oplus {\boldsymbol {a}}&x_{0}=1\end{cases}}}
where x0 is the lowest order bit of x.

As like TGFSR(R), the Mersenne Twister is cascaded with a tempering transform to compensate for the reduced dimensionality of equidistribution (because of the choice of A being in the rational normal form). Note that this is equivalent to using the matrix A where A = T−1AT for T an invertible matrix, and therefore the analysis of characteristic polynomial mentioned below still holds.

As with A, we choose a tempering transform to be easily computable, and so do not actually construct T itself. The tempering is defined in the case of Mersenne Twister as

{\displaystyle {\begin{aligned}y&\equiv x\oplus ((x\gg u)~\And ~d)\\y&\equiv y\oplus ((y\ll s)~\And ~b)\\y&\equiv y\oplus ((y\ll t)~\And ~c)\\z&\equiv y\oplus (y\gg l)\end{aligned}}}{\displaystyle {\begin{aligned}y&\equiv x\oplus ((x\gg u)~\And ~d)\\y&\equiv y\oplus ((y\ll s)~\And ~b)\\y&\equiv y\oplus ((y\ll t)~\And ~c)\\z&\equiv y\oplus (y\gg l)\end{aligned}}}

where x is the next value from the series, y a temporary intermediate value, z the value returned from the algorithm, with ≪, ≫ as the bitwise left and right shifts, and & as the bitwise and. The first and last transforms are added in order to improve lower-bit equidistribution. From the property of TGFSR, s + t ≥ ⌊w/2⌋ − 1 is required to reach the upper bound of equidistribution for the upper bits.

The coefficients for MT19937 are:

(w, n, m, r) = (32, 624, 397, 31)
a = 9908B0DF16
(u, d) = (11, FFFFFFFF16)
(s, b) = (7, 9D2C568016)
(t, c) = (15, EFC6000016)
l = 18
Note that 32-bit implementations of the Mersenne Twister generally have d = FFFFFFFF16. As a result, the d is occasionally omitted from the algorithm description, since the bitwise and with d in that case has no effect.

The coefficients for MT19937-64 are:

(w, n, m, r) = (64, 312, 156, 31)
a = B5026F5AA96619E916
(u, d) = (29, 555555555555555516)
(s, b) = (17, 71D67FFFEDA6000016)
(t, c) = (37, FFF7EEE00000000016)
l = 43
Initialization
The state needed for a Mersenne Twister implementation is an array of n values of w bits each. To initialize the array, a w-bit seed value is used to supply x0 through xn−1 by setting x0 to the seed value and thereafter setting

{\displaystyle x_{i}=f\times (x_{i-1}\oplus (x_{i-1}\ll (w-2))+i}{\displaystyle x_{i}=f\times (x_{i-1}\oplus (x_{i-1}\ll (w-2))+i}

for i from 1 to n − 1.

The first value the algorithm then generates is based on xn, not on x0.
The constant f forms another parameter to the generator, though not part of the algorithm proper.
The value for f for MT19937 is 1812433253.
The value for f for MT19937-64 is 6364136223846793005.[53]
Comparison with classical GFSR
In order to achieve the 2nw−r − 1 theoretical upper limit of the period in a TGFSR, φB(t) must be a primitive polynomial, φB(t) being the characteristic polynomial of

{\displaystyle B={\begin{pmatrix}0&I_{w}&\cdots &0&0\\\vdots &&&&\\I_{w}&\vdots &\ddots &\vdots &\vdots \\\vdots &&&&\\0&0&\cdots &I_{w}&0\\0&0&\cdots &0&I_{w-r}\\S&0&\cdots &0&0\end{pmatrix}}{\begin{matrix}\\\\\leftarrow m{\hbox{-th row}}\\\\\\\\\end{matrix}}}B={\begin{pmatrix}0&I_{w}&\cdots &0&0\\\vdots &&&&\\I_{w}&\vdots &\ddots &\vdots &\vdots \\\vdots &&&&\\0&0&\cdots &I_{w}&0\\0&0&\cdots &0&I_{w-r}\\S&0&\cdots &0&0\end{pmatrix}}{\begin{matrix}\\\\\leftarrow m{\hbox{-th row}}\\\\\\\\\end{matrix}}

{\displaystyle S={\begin{pmatrix}0&I_{r}\\I_{w-r}&0\end{pmatrix}}A}S={\begin{pmatrix}0&I_{r}\\I_{w-r}&0\end{pmatrix}}A

The twist transformation improves the classical GFSR with the following key properties:

The period reaches the theoretical upper limit 2nw−r − 1 (except if initialized with 0)
Equidistribution in n dimensions (e.g. linear congruential generators can at best manage reasonable distribution in five dimensions)