import argparse
def to_fahrenheit(tempC):
    return (9/5) * tempC + 32
def to_celsius(tempF):
    return (5/9) * (tempF - 32)
def main():
    parser = argparse.ArgumentParser(
        description="Temperature Converter"
    )
    key = parser.add_mutually_exclusive_group(required=True)

    key.add_argument(
        "-c", "--celsius",
        type=float,
        metavar="TEMP",
        help="Convert Celsius (TEMP) to Fahrenheit"
    )

    key.add_argument(
        "-f", "--fahrenheit",
        type=float,
        metavar="TEMP",
        help="Convert Fahrenheit (TEMP) to Celsius"
    )

    args = parser.parse_args()

    if args.celsius is not None:
        fahrenheit = to_fahrenheit(args.celsius)
        print(f"{args.celsius:.2f}°C = {fahrenheit:.2f}°F")
    elif args.fahrenheit is not None:
        celsius = to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit:.2f}°F = {celsius:.2f}°C")

if __name__ == "__main__":
    main()
