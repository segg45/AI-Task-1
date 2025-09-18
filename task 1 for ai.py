import random

#Step 1: Defining the function to minimize
def f(x, y):
    return (x**2 - y + 11)**2 + (x + y**2 - 7)**2

#Step 2: Implementing Randomized Hill Climbing
def RHC(sp, p, z, seed):
    random.seed(seed)
    x, y = sp
    best_val = f(x, y)
    best_point = (x, y)
    total_solutions = 0

    while True:
        improved = False
        neighbors = []

        for _ in range(p):
            dx = random.uniform(-z, z)
            dy = random.uniform(-z, z)
            nx = max(min(x + dx, 6), -6)
            ny = max(min(y + dy, 6), -6)
            neighbors.append((nx, ny))

        total_solutions += len(neighbors)

        for nx, ny in neighbors:
            val = f(nx, ny)
            if val < best_val:
                best_val = val
                best_point = (nx, ny)
                x, y = nx, ny
                improved = True
                break  # move for better neighbor

        if not improved:
            break

    return best_point, best_val, total_solutions

#Step 3: Defining parameters
starting_points = [(2.9, 3.2), (-2.5, 3.2), (4.2, -2), (-5, -5)]
p_values = [30, 180]
z_values = [0.03, 0.1]
seeds = [42, 43]

#Step 4: Run all combinations and store results
results = []

for p in p_values:
    for z in z_values:
        for sp in starting_points:
            for seed in seeds:
                best_point, best_val, total_solutions = RHC(sp, p, z, seed)
                results.append({
                    'p': p,
                    'z': z,
                    'sp': sp,
                    'seed': seed,
                    'best_point': best_point,
                    'f_value': best_val,
                    'solutions_generated': total_solutions
                })

#Step 5: Tables for results
def print_table(p, z, results):
    print(f"\nTable for p = {p}, z = {z}")
    print(f"{'Start Point':>15} | {'Seed':>4} | {'Best (x,y)':>20} | {'f(x,y)':>10} | {'# Solutions':>12}")
    print("-" * 70)
    for r in results:
        if r['p'] == p and r['z'] == z:
            sp = f"({r['sp'][0]:.2f}, {r['sp'][1]:.2f})"
            bp = f"({r['best_point'][0]:.4f}, {r['best_point'][1]:.4f})"
            print(f"{sp:>15} | {r['seed']:>4} | {bp:>20} | {r['f_value']:>10.4f} | {r['solutions_generated']:>12}")

#Step 6: Print tables
for p in p_values:
    for z in z_values:
        print_table(p, z, results)

#Bonus: Run #33

print("\n" + "="*70)
print("Run #33 - Custom Parameters")
print("="*70)

sp = (4.2, -2)
p = 300
z = 0.07
seed = 99

best_point, best_val, total_solutions = RHC(sp, p, z, seed)

print(f"Start Point: ({sp[0]}, {sp[1]})")
print(f"Best Point: ({best_point[0]:.4f}, {best_point[1]:.4f})")
print(f"f(x, y): {best_val:.4f}")
print(f"Solutions Generated: {total_solutions}")
