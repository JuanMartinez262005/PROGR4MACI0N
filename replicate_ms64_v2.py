import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Estilo académico
plt.rcParams.update({"font.family": "serif", "axes.labelsize": 10, "grid.alpha": 0.2})

def plot_fig_6b(df):
    """Tasas de cambio de temperatura (Balance de Calor)"""
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.plot(df['rate_lh2o'], df['altitude_km'], 'k--', label='$LH_2O$ (Infrared)')
    ax.plot(df['rate_lco2'], df['altitude_km'], 'k:', label='$LCO_2$')
    ax.plot(df['rate_lo3'], df['altitude_km'], 'k-', alpha=0.5, label='$LO_3$')
    ax.plot(df['rate_sho3'], df['altitude_km'], 'k-', label='$SO_3$ (Solar)')
    
    ax.axvline(0, color='k', lw=0.8)
    ax.set_xlabel('Rate of Temp. Change (°C/day)')
    ax.set_ylabel('Altitude (km)')
    ax.set_title('Figure 6b: Heat Balance Components')
    ax.legend(loc='upper left', frameon=False)
    ax.set_ylim(0, 42)
    plt.tight_layout()
    plt.savefig('figures/Figure_6b.png', dpi=300)
    plt.savefig('figures/Figure_6b.pdf')

def plot_fig_6c(df):
    """Equilibrio térmico (6.5°C/km) con distintos gases"""
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.plot(df['t_6c_h2o'], df['pressure_mb'], 'k:', label='$H_2O$')
    ax.plot(df['t_6c_h2o_co2'], df['pressure_mb'], 'k--', label='$H_2O + CO_2$')
    ax.plot(df['t_6c_full'], df['pressure_mb'], 'k-', label='$H_2O + CO_2 + O_3$')
    
    ax.set_yscale('log')
    ax.invert_yaxis()
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Pressure (mb)')
    ax.set_title('Figure 6c: Thermal Equilibrium (6.5°C/km)')
    ax.legend()
    plt.tight_layout()
    plt.savefig('figures/Figure_6c.png', dpi=300)
    plt.savefig('figures/Figure_6c.pdf')

def plot_fig_6d(df):
    """Equilibrio sin sol (Invierno Ártico)"""
    fig, ax = plt.subplots(figsize=(5, 7))
    ax.plot(df['t_6d_rad_289'], df['pressure_mb'], 'k--', label='Pure Rad. (289K surf)')
    ax.plot(df['t_6d_conv_289'], df['pressure_mb'], 'k-', label='Thermal Equil. (289K)')
    ax.plot(df['t_6d_conv_263'], df['pressure_mb'], 'k-.', label='Thermal Equil. (263K)')
    
    ax.set_yscale('log')
    ax.invert_yaxis()
    ax.set_xlabel('Temperature (K)')
    ax.set_title('Figure 6d: Equilibrium without Insolation')
    ax.legend()
    plt.tight_layout()
    plt.savefig('figures/Figure_6d.png', dpi=300)
    plt.savefig('figures/Figure_6d.pdf')

if __name__ == '__main__':
    os.makedirs('figures', exist_ok=True)
    df = pd.read_csv('data/digitized_profiles_v2.csv')
    plot_fig_6b(df)
    plot_fig_6c(df)
    plot_fig_6d(df)