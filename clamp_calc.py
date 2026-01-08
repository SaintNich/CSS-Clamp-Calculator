import argparse

def precision_fmt(value, precision=3):
    return f"{value:.{precision}f}".rstrip("0").rstrip(".")

def calculate_clamp(min_size, max_size, vw_min, vw_max, root_font = 16, precision = 3):
    min_size = float(min_size)
    max_size = float(max_size)
    vw_min = float(vw_min)
    vw_max = float(vw_max)

    if min_size <=0 or max_size <= 0 or vw_min <=0 or vw_max <= 0:
        raise ValueError("All inputs must be positive.")
    if max_size < min_size:
        raise ValueError("Maximum size must be greater than or equal to minimum size.")
    if vw_max <= vw_min:
        raise ValueError("Maximum viewport must be greater than minimum viewport")

    min_size_px = (root_font * min_size)
    max_size_px = (root_font * max_size)
    slope = ((max_size_px - min_size_px) / (vw_max - vw_min))
    slope_vw = (slope * 100)
    intercept = (min_size_px - (slope * vw_min))
    int_rem = (intercept / root_font)
    css = f"clamp({precision_fmt(min_size, precision)}rem, {precision_fmt(int_rem, precision)}rem + {precision_fmt(slope_vw, precision)}vw, {precision_fmt(max_size, precision)}rem)"

    return {
        "min": min_size,
        "max": max_size,
        "slope": slope_vw,
        "intercept": int_rem,
        "css":css
    }

def get_val(name: str, current_value: str | None, prompt: str):
    if current_value is not None and str(current_value).strip() != "":
        return str(current_value).strip()
    return input(prompt).strip()

def main():
    parser = argparse.ArgumentParser(description="CSS clamp() calculator")
    parser.add_argument("--min", dest="min_size", help="Minimum font-size in rem")
    parser.add_argument("--max", dest="max_size", help="Maximum font-size in rem")
    parser.add_argument("--vw-min", dest="vw_min", help="Minimum viewport width in px")
    parser.add_argument("--vw-max", dest="vw_max", help="Maximum viewport width in px")
    parser.add_argument("--precision", type=int, default=3, help="Decimal places for output (default = 3)")
    args = parser.parse_args()
    
    min_size = get_val("min", args.min_size, ("What's the minimum size in rem? "))
    max_size = get_val("max", args.max_size, ("What's the maximum size in rem? "))
    vw_min = get_val("vw-min", args.vw_min, ("What's the minimum viewport's width in px? "))
    vw_max = get_val("vw-max", args.vw_max, ("What's the maximum viewport's width in px? "))

    try:
        result = calculate_clamp(min_size, max_size, vw_min, vw_max, precision=args.precision)
        print(result["css"])
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()