"""
 Methods for Integrating Functions

   odeint        -- Integrate ordinary differential equations.
   quad          -- General purpose integration.
   dblquad       -- General purpose double integration.
   tplquad       -- General purpose triple integration.
   gauss_quad    -- Integrate func(x) using Gaussian quadrature of order n.
   gauss_quadtol -- Integrate with given tolerance using Gaussian quadrature.


   See the orthogonal module (scipy.integrate.orthogonal) for Gaussian
      quadrature roots and weights.
"""
_moddict = {'quadrature': ['gauss_quad', 'gauss_quadtol','romberg'],
            'odepack': ['odeint'],
            'quadpack': ['quad', 'dblquad', 'tplquad', 'quad_explain', 'Inf',
                         'inf']
            }

__all__ = []
import scipy
scipy.somenames2all(__all__, _moddict, globals())
scipy.modules2all(__all__, ['orthogonal'], globals())
del scipy
