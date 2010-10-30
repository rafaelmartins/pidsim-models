# -*- coding: utf-8 -*-
"""
    pidsim_models.models
    ~~~~~~~~~~~~~~~~~~~~

    Models implementation.

    :copyright: 2010 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

from pidsim.types import tf, poly
from pidsim_models.base import ReferenceModel, I18nStr

class Model1(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de primeira ordem'),
    ])
    
    latex = 'G_p(s) = \\frac{k}{(1+\\tau s)}'
    
    def callback(self, k, Tau):
        return tf([k], [Tau, 1])


class Model2(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de segunda ordem'),
    ])
    
    latex = 'G_p(s) = \\frac{k}{(1+T_1 s)(1+T_2 s)}'
    
    def callback(self, k, T1, T2):
        return tf([k], poly([T1, 1]) * poly([T2, 1]))


class Model3(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de segunda ordem de fase não-mínima'),
    ])
    
    latex = 'G_p(s) = \\frac{k(1-T_1 s)}{(1+T_1 s)(1+T_2 s)}'
    
    def callback(self, k, T1, T2):
        return tf([-T1 * k, k], poly([T1, 1]) * poly([T2, 1]))


class Model4(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de terceira ordem com tempo morto ajustável'),
    ])
    
    latex = 'G_p(s) = \\frac{k(1+T_4 s)}{(1+T_1 s)(1+T_2 s)(1+T_3 s)} e^{-T_t s}'
    
    def callback(self, k, T1, T2, T3, T4, Tt):
        return tf([], [])


class Model5(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de pólos múltiplos e iguais'),
    ])
    
    latex = 'G_p(s) = \\frac{1}{(s+1)^n}'
    
    def callback(self, n):
        a = poly([1, 1])
        for i in range(1, int(n)):
            a = a * poly([1, 1])
        return tf([1], list(a))


class Model6(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de quarta ordem'),
    ])
    
    latex = 'G_p(s) = \\frac{1}{(s+1)(\\alpha s+1)(\\alpha ^2 s+1)(\\alpha ^3 s+1)}'
    
    def callback(self, Alpha):
        num = (pol([1, 1]) * poly([Alpha, 1])) * (poly([Alpha * Alpha, 1]) * \
            pol([Alpha * Alpha * Alpha, 1]))
        return tf([1], num)


class Model7(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo com três pólos iguais e zero no semi-plano direito'),
    ])
    
    latex = 'G_p(s) = \\frac{1-\\alpha s}{(s+1)^3}'
    
    def callback(self, Alpha):
        return tf([-Alpha, 1], (pol([1, 1]) * pol([1, 1])) * pol([1, 1]))


class Model8(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de primeira ordem com tempo morto'),
    ])
    
    latex = 'G_p(s) = \\frac{1}{(\\tau s +1)}e^{-s}'
    
    def callback(self, Tau):
        return tf([], [])


class Model9(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de segunda ordem com tempo morto'),
    ])
    
    latex = 'G_p(s) = \\frac{1}{(\\tau s +1)^2}e^{-s}'
    
    def callback(self, Tau):
        return tf([], [])


class Model10(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo com características dinâmicas assimétricas'),
    ])
    
    latex = 'G_p(s) = \\frac{100}{(s+10)^2}\\left ( \\frac{1}{s+1} + \\frac{0,5}{s+0,05} \\right )'
    
    def callback(self):
        den = (poly([1, 10]) * poly([1, 10])) * (tf([1], [1, 1]) + \
            tf([0.5], [1, 0.05]))
        return tf([100], den)


class Model11(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo condicionalmente estável'),
    ])
    
    latex = 'G_p(s) = \\frac{(s+6)^2}{s(s+1)^2 (s+36)}'
    
    def callback(self):
        den = (poly([1, 0]) * poly([1, 1])) * (poly([1, 1]) * poly([1, 36]))
        return tf(poly([1, 6]) * poly([1, 6]), den)


class Model12(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo oscilatório'),
    ])
    
    latex = 'G_p(s) = \\frac{\\omega _0^2}{(s+1)(s^2+2\\zeta \\omega _0 s+\\omega _0^2)}'
    
    def callback(self, Omega, Zeta):
        return tf([Omega * Omega], poly([1, 1]) * poly([1, 2 * Zeta * Omega, Omega * Omega]))


class Model13(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo instável'),
    ])
    
    latex = 'G_p(s) = \\frac{1}{s^2 - 1}'
    
    def callback(self):
        return tf([1], [1, 0, -1])


class Model14(ReferenceModel):
    
    name = I18nStr([
        ('pt_BR', u'Processo de primeira ordem mais tempo morto com a presença de integrador'),
    ])
    
    latex = 'G_p(s) = \\frac{1}{s(\\tau s + 1)}e^{-s}'
    
    def callback(self, Tau):
        return tf([], [])

models = {
    1: Model1,
    2: Model2,
    3: Model3,
    4: None, #Model4,
    5: Model5,
    6: Model6,
    7: Model7,
    8: None, #Model8,
    9: None, #Model9,
    10: Model10,
    11: Model11,
    12: Model12,
    13: Model13,
    14: None, #Model14,
}