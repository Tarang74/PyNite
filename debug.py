from numpy import where, append, array, empty, float, delete, squeeze, size
func = '''(Abs, acos, acosh, acot, acoth, acsc, acsch, adjoint, airyai,
            airyaiprime, airybi, airybiprime, appellf1, arg, asec, asech, asin,
            asinh, assoc_laguerre, assoc_legendre, atan, atan2, atanh, bell,
            bernoulli, besseli, besselj, besselk, bessely, beta, binomial,
            bspline_basis, bspline_basis_set, carmichael, catalan, cbrt,
            ceiling, chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
            Chi, Ci, combinatorial, conjugate, cos, cosh, cot, coth, csc, csch,
            digamma, DiracDelta, dirichlet_eta, E1, Ei, Eijk, elementary,
            elliptic_e, elliptic_f, elliptic_k, elliptic_pi, erf, erf2,
            erf2inv, erfc, erfcinv, erfi, erfinv, euler, exp, exp_polar,
            expint, factorial, factorial2, FallingFactorial, ff, fibonacci,
            floor, frac, fresnelc, fresnels, gamma, gegenbauer, genocchi,
            hankel1, hankel2, harmonic, Heaviside, hermite, hn1, hn2, hyper,
            Id, im, interpolating_spline, jacobi, jacobi_normalized, jn,
            jn_zeros, KroneckerDelta, laguerre, LambertW, legendre, lerchphi,
            LeviCivita, Li, li, ln, log, loggamma, lowergamma, lucas, marcumq,
            mathieuc, mathieucprime, mathieus, mathieusprime, Max, meijerg,
            Min, multigamma, partition, periodic_argument, Piecewise,
            piecewise_fold, polar_lift, polarify, polygamma, polylog,
            principal_branch, re, real_root, rf, RisingFactorial, root, sec,
            sech, Shi, Si, sign, sin, sinc, SingularityFunction, sinh, special,
            sqrt, stieltjes, subfactorial, tan, tanh, transpose, tribonacci,
            trigamma, unbranched_argument, unpolarify, uppergamma, yn, Ynm,
            Ynm_c, zeta, Znm)'''
from sympy import E, pi, I
exec("from sympy.functions import " + func)


class Debug():
    def debug(self):
        self.appNodes = array([['name', '1', '1', '1'],
                               ['name2', '2', '1', '1'],
                               ['name3', '3', '1', '1']])
        self.appMembers = array([['a', '0', '1', '0'], ['ab', '0', '2', '0']])
        self.appMaterials = array([['mat1', '1', '1']])

    def debug1(self):
        expr = '-001.100002500*9'
        expr = float(re(eval(expr)))
        print(expr)


ui = Debug()
ui.debug1()
