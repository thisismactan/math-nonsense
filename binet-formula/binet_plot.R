library(tidyverse)

# Binet's formula for the nth Fibonacci number
binet <- function(x) {
  phi <- (1 + sqrt(5)) / 2
  psi <- -1 / phi
  
  return((phi^x - psi^x) / sqrt(5))
}

# Grid of values
coords_grid <- expand.grid(x = seq(from = -30, to = 30, by = 0.05),
                           y = seq(from = -10, to = 10, by = 0.05)) %>%
  as_tibble() %>%
  
  # Compute Binet formula and modulus (magnitude) and argument (angle)
  mutate(binet = binet(complex(real = x, imaginary = y)),
         magnitude = Mod(binet),
         angle = Arg(binet))

# Pretty plot
coords_grid %>%
  ggplot(aes(x = x, y = y)) +
  geom_point(aes(col = angle), show.legend = FALSE) +
  geom_vline(xintercept = 0) + 
  geom_hline(yintercept = 0) +
  scale_colour_gradientn(colours = c("#FF0000", "#FFFF00", "#00FF00", "#00FFFF", "#0000FF", "#FF0000"),
                         breaks = c(0, pi/3, 2 * pi/3, 3 * pi/3, 4 * pi/3, 5 * pi/3, 6 * pi/3)) +
  scale_x_continuous(breaks = (-30):30) +
  scale_y_continuous(breaks = (-10):10) +
  labs(x = "Real", y = "Imaginary")

ggsave("binet_function.png", width = 1600/100, height = 800/100, dpi = 100)
